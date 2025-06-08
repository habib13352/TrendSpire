#!/usr/bin/env python3
"""Automation orchestrator for TrendSpire Codex workflows."""

import argparse
import os
import subprocess
import sys
import tempfile
import shutil
from datetime import datetime

try:
    from dotenv import load_dotenv

    env_path = os.path.join(os.getcwd(), ".env")
    if os.path.isfile(env_path):
        load_dotenv(dotenv_path=env_path)
except ImportError:
    pass

from openai import OpenAI, OpenAIError
import tiktoken
from ai_loop.utils_common import (
    ensure_logs,
    count_tokens,
    run_cmd,
    is_valid_diff,
    is_suspicious_deletion,
    append_cost,
    write_summary,
    load_prompt,
    rollback_if_tests_fail,
)


def get_openai_client() -> OpenAI:
    """Create an OpenAI client using the environment variable."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in environment")
    return OpenAI(api_key=api_key)


client = get_openai_client()

from ai_loop.api_logger import log_openai_usage

LOG_DIR = "codex_logs"
COST_LOG = "codex_costs.csv"

DAILY_MODEL = "gpt-3.5-turbo"
DAILY_RATE = 0.002 / 1000  # $0.002 per 1K tokens

WEEKLY_MODEL = "gpt-4o"
WEEKLY_RATE = 0.005 / 1000  # Adjusted for gpt-4o pricing
SOURCE_DIR = "src"
MEMORY_DIR = "trendspire_memory"
LAST_SUMMARY = os.path.join(MEMORY_DIR, "last_summary.md")




def daily_run() -> None:
    """Run the daily diff-based Codex automation."""
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    subprocess.run(["git", "fetch", "origin", "main"], check=False)
    subprocess.run(["git", "checkout", "main"], check=False)
    subprocess.run(["git", "pull", "origin", "main", "--rebase"], check=False)

    diff_proc = run_cmd(["git", "diff", "origin/main...HEAD", "--", SOURCE_DIR])
    diff_text = diff_proc.stdout

    template = load_prompt("daily.diff.j2")
    prompt = template.replace("{{ diff }}", diff_text)

    try:
        response = client.chat.completions.create(
            model=DAILY_MODEL,
            messages=[{"role": "user", "content": prompt}],
        )
        diff_response = response.choices[0].message.content
        used_model = DAILY_MODEL
        used_rate = DAILY_RATE
    except OpenAIError as e:
        print(f"Primary model failed: {e}. Falling back to gpt-3.5-turbo.")
        try:
            fallback_model = "gpt-3.5-turbo"
            fallback_rate = 0.002 / 1000
            response = client.chat.completions.create(
                model=fallback_model,
                messages=[{"role": "user", "content": prompt}],
            )
            diff_response = response.choices[0].message.content
            used_model = fallback_model
            used_rate = fallback_rate
        except OpenAIError as e2:
            print(f"Fallback model also failed: {e2}", file=sys.stderr)
            return

    if not diff_response.strip():
        print("No diff returned from API", file=sys.stderr)
        return

    prompt_tokens = count_tokens(prompt, used_model)
    completion_tokens = count_tokens(diff_response, used_model)
    cost = (prompt_tokens + completion_tokens) * used_rate

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".diff")
    tmp.write(diff_response.encode("utf-8"))
    tmp.close()

    if not is_valid_diff(diff_response):
        print("Invalid diff detected from AI output — skipping git apply.", file=sys.stderr)
        broken_path = os.path.join(LOG_DIR, f"invalid_diff_{timestamp}.txt")
        with open(broken_path, "w", encoding="utf-8") as f:
            f.write(diff_response)
        return
    if is_suspicious_deletion(diff_response):
        print("Suspicious deletion detected in diff. Skipping.", file=sys.stderr)
        broken_path = os.path.join(LOG_DIR, f"suspicious_diff_{timestamp}.diff")
        with open(broken_path, "w", encoding="utf-8") as f:
            f.write(diff_response)
        return
    try:
        run_cmd(["git", "apply", tmp.name])
    except RuntimeError as exc:
        broken_path = os.path.join(LOG_DIR, f"broken_diff_{timestamp}.diff")
        with open(broken_path, "w", encoding="utf-8") as f:
            f.write(diff_response)
        print(exc, file=sys.stderr)
        return

    try:
        test_proc = run_cmd(["pytest", "--maxfail=1", "--disable-warnings"])
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return

    summary_path = os.path.join(LOG_DIR, f"summary_{timestamp}_daily.md")
    snippet = "\n".join(diff_response.splitlines()[:20])
    write_summary(summary_path, used_model, "daily", (prompt_tokens, completion_tokens), cost, test_proc.stdout, snippet)
    append_cost(timestamp, "daily", (prompt_tokens, completion_tokens), used_model, cost, COST_LOG)
    log_openai_usage(used_model, prompt_tokens, completion_tokens, cost)

    if test_proc.returncode == 0:
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not status.stdout.strip():
            print("No changes produced", file=sys.stderr)
            return
        branch = f"codex-daily-{timestamp}"
        diff_memory_path = os.path.join(MEMORY_DIR, f"diff_{timestamp}.diff")
        with open(diff_memory_path, "w", encoding="utf-8") as f:
            f.write(diff_response)
        subprocess.run(["git", "checkout", "-b", branch], check=True)
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run([
            "git",
            "commit",
            "-m",
            f"chore: daily Codex improvements {timestamp}",
        ], check=True)
        try:
            rollback_if_tests_fail()
        except RuntimeError as exc:
            print(exc, file=sys.stderr)
            return
        subprocess.run(["git", "push", "origin", branch], check=False)
        run_cmd([
            "gh",
            "pr",
            "create",
            "--fill",
            "--title",
            f"chore: daily Codex improvements {timestamp}",
        ])
    else:
        sys.exit(test_proc.returncode)


def weekly_run() -> None:
    """Run the weekly full-repo Codex automation."""
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    subprocess.run(["git", "fetch", "origin", "main"], check=False)
    subprocess.run(["git", "checkout", "main"], check=False)
    subprocess.run(["git", "pull", "origin", "main", "--rebase"], check=False)

    files = []
    for root, _dirs, filenames in os.walk(SOURCE_DIR):
        for name in filenames:
            if name.endswith(".py"):
                files.append(os.path.join(root, name))

    code_parts = []
    for path in sorted(files):
        with open(path, "r", encoding="utf-8") as f:
            code_parts.append(f"# File: {path}\n" + f.read())

    full_code = "\n\n".join(code_parts)
    review_context = ""
    if os.path.exists(LAST_SUMMARY):
        with open(LAST_SUMMARY, "r", encoding="utf-8") as f:
            last_summary = f.read()
        review_context = (
            "Here's the last change I made to the codebase:\n\n" + last_summary
            + "\n\nNow, review your own changes and suggest further improvements. "
            "Look for any inefficiencies, or opportunities to add tests, better logging, docstrings, or simplify the logic.\n\n"
        )
    template = load_prompt("weekly.refactor.j2")
    prompt = (
        template.replace("{{ review_context }}", review_context).replace(
            "{{ full_code }}",
            full_code,
        )
    )

    try:
        response = client.chat.completions.create(
            model=WEEKLY_MODEL,
            messages=[{"role": "user", "content": prompt}],
        )
        diff_response = response.choices[0].message.content
        used_model = WEEKLY_MODEL
        used_rate = WEEKLY_RATE
    except OpenAIError as e:
        print(f"Primary model failed: {e}. Falling back to gpt-3.5-turbo.")
        try:
            fallback_model = "gpt-3.5-turbo"
            fallback_rate = 0.002 / 1000
            response = client.chat.completions.create(
                model=fallback_model,
                messages=[{"role": "user", "content": prompt}],
            )
            diff_response = response.choices[0].message.content
            used_model = fallback_model
            used_rate = fallback_rate
        except OpenAIError as e2:
            print(f"Fallback model also failed: {e2}", file=sys.stderr)
            return

    if not diff_response.strip():
        print("No diff returned from API", file=sys.stderr)
        return

    prompt_tokens = count_tokens(prompt, used_model)
    completion_tokens = count_tokens(diff_response, used_model)
    cost = (prompt_tokens + completion_tokens) * used_rate

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".diff")
    tmp.write(diff_response.encode("utf-8"))
    tmp.close()

    if not is_valid_diff(diff_response):
        print("Invalid diff detected from AI output — skipping git apply.", file=sys.stderr)
        broken_path = os.path.join(LOG_DIR, f"invalid_diff_{timestamp}.txt")
        with open(broken_path, "w", encoding="utf-8") as f:
            f.write(diff_response)
        return

    if is_suspicious_deletion(diff_response):
        print("Suspicious deletion detected in diff. Skipping.", file=sys.stderr)
        broken_path = os.path.join(LOG_DIR, f"suspicious_diff_{timestamp}.diff")
        with open(broken_path, "w", encoding="utf-8") as f:
            f.write(diff_response)
        return
    try:
        run_cmd(["git", "apply", tmp.name])
    except RuntimeError as exc:
        broken_path = os.path.join(LOG_DIR, f"broken_diff_{timestamp}.diff")
        with open(broken_path, "w", encoding="utf-8") as f:
            f.write(diff_response)
        print(exc, file=sys.stderr)
        return

    try:
        test_proc = run_cmd(["pytest"])
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return

    summary_path = os.path.join(LOG_DIR, f"summary_{timestamp}_weekly.md")
    snippet = "\n".join(diff_response.splitlines()[:20])
    write_summary(summary_path, used_model, "weekly", (prompt_tokens, completion_tokens), cost, test_proc.stdout, snippet)
    append_cost(timestamp, "weekly", (prompt_tokens, completion_tokens), used_model, cost, COST_LOG)
    log_openai_usage(used_model, prompt_tokens, completion_tokens, cost)

    if test_proc.returncode == 0:
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not status.stdout.strip():
            print("No changes produced", file=sys.stderr)
            return
        branch = f"codex-weekly-{timestamp}"
        diff_memory_path = os.path.join(MEMORY_DIR, f"diff_{timestamp}.diff")
        with open(diff_memory_path, "w", encoding="utf-8") as f:
            f.write(diff_response)
        shutil.copy(summary_path, LAST_SUMMARY)
        subprocess.run(["git", "checkout", "-b", branch], check=True)
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run([
            "git",
            "commit",
            "-m",
            f"chore: weekly Codex improvements {timestamp}",
        ], check=True)
        try:
            rollback_if_tests_fail()
        except RuntimeError as exc:
            print(exc, file=sys.stderr)
            return
        subprocess.run(["git", "push", "origin", branch], check=False)
        run_cmd([
            "gh",
            "pr",
            "create",
            "--fill",
            "--title",
            f"chore: weekly Codex improvements {timestamp}",
        ])
    else:
        sys.exit(test_proc.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Codex automations")
    parser.add_argument(
        "--mode",
        choices=["daily", "weekly"],
        required=True,
        help="Choose 'daily' for diff-only runs or 'weekly' for full-repo runs."
    )
    args = parser.parse_args()
    ensure_logs(LOG_DIR, COST_LOG, MEMORY_DIR)

    if args.mode == "daily":
        daily_run()
    else:
        weekly_run()


if __name__ == "__main__":
    main()
