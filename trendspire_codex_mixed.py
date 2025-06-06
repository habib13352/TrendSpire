#!/usr/bin/env python3
"""Automation orchestrator for TrendSpire Codex workflows."""

import argparse
import os
import subprocess
import sys
import tempfile
from datetime import datetime

from dotenv import load_dotenv
import openai
import tiktoken

from src.api_logger import log_openai_usage

LOG_DIR = "codex_logs"
COST_LOG = "codex_costs.csv"

DAILY_MODEL = "gpt-3.5-turbo"
DAILY_RATE = 0.002 / 1000
WEEKLY_MODEL = "code-davinci-002"
WEEKLY_RATE = 0.02 / 1000
SOURCE_DIR = "src"


def ensure_logs():
    """Create logging directories and cost file if missing."""
    os.makedirs(LOG_DIR, exist_ok=True)
    if not os.path.exists(COST_LOG):
        with open(COST_LOG, "w", encoding="utf-8") as f:
            f.write("timestamp,run_type,prompt_tokens,completion_tokens,model,cost_usd\n")


def count_tokens(text: str, model: str) -> int:
    """Count tokens for the given model."""
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))


def run_cmd(cmd):
    """Run a shell command and capture output."""
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def write_summary(path: str, model: str, run_type: str, tokens: tuple, cost: float, test_output: str, diff_snippet: str) -> None:
    """Write markdown summary report."""
    prompt_tokens, completion_tokens = tokens
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"## {run_type.capitalize()} Codex Run {datetime.utcnow().isoformat()}\n\n")
        f.write(f"Model: {model}\n\n")
        f.write(f"Prompt tokens: {prompt_tokens}\n")
        f.write(f"Completion tokens: {completion_tokens}\n")
        f.write(f"Cost: ${cost:.6f}\n\n")
        f.write("### Test Output\n")
        f.write(f"```\n{test_output}\n```\n")
        f.write("### Diff Snippet\n")
        f.write(f"```diff\n{diff_snippet}\n```\n")


def append_cost(timestamp: str, run_type: str, tokens: tuple, model: str, cost: float) -> None:
    """Append cost information to CSV log."""
    prompt_tokens, completion_tokens = tokens
    with open(COST_LOG, "a", encoding="utf-8") as f:
        f.write(f"{timestamp},{run_type},{prompt_tokens},{completion_tokens},{model},{cost:.6f}\n")


def daily_run() -> None:
    """Run the daily diff-based Codex automation."""
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    subprocess.run(["git", "fetch", "origin", "main"], check=False)

    diff_proc = run_cmd(["git", "diff", "origin/main...HEAD", "--", SOURCE_DIR])
    diff_text = diff_proc.stdout

    prompt = (
        "Based on this diff, propose pytest test files, small refactors, and logging statements. "
        "Return a unified git diff. Do not output anything else.\n\n" + diff_text
    )
    prompt_tokens = count_tokens(prompt, DAILY_MODEL)

    openai.api_key = os.environ.get("OPENAI_API_KEY")
    try:
        response = openai.ChatCompletion.create(model=DAILY_MODEL, messages=[{"role": "user", "content": prompt}])
        diff_response = response.choices[0].message.content
    except Exception as exc:
        print(f"OpenAI API error: {exc}", file=sys.stderr)
        sys.exit(1)

    completion_tokens = count_tokens(diff_response, DAILY_MODEL)
    cost = (prompt_tokens + completion_tokens) * DAILY_RATE

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".diff")
    tmp.write(diff_response.encode("utf-8"))
    tmp.close()

    apply_proc = run_cmd(["git", "apply", tmp.name])
    if apply_proc.returncode != 0:
        broken_path = os.path.join(LOG_DIR, f"broken_diff_{timestamp}.diff")
        with open(broken_path, "w", encoding="utf-8") as f:
            f.write(diff_response)
        print(apply_proc.stderr, file=sys.stderr)
        sys.exit(1)

    test_proc = run_cmd(["pytest", "--maxfail=1", "--disable-warnings"])

    summary_path = os.path.join(LOG_DIR, f"summary_{timestamp}_daily.md")
    snippet = "\n".join(diff_response.splitlines()[:20])
    write_summary(summary_path, DAILY_MODEL, "daily", (prompt_tokens, completion_tokens), cost, test_proc.stdout, snippet)
    append_cost(timestamp, "daily", (prompt_tokens, completion_tokens), DAILY_MODEL, cost)
    log_openai_usage(DAILY_MODEL, prompt_tokens, completion_tokens, cost)

    if test_proc.returncode == 0:
        branch = f"codex-daily-{timestamp}"
        subprocess.run(["git", "checkout", "-b", branch], check=True)
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run(["git", "commit", "-m", f"chore: daily Codex improvements {timestamp}"], check=True)
        subprocess.run(["git", "push", "origin", branch], check=False)
        run_cmd(["gh", "pr", "create", "--fill", "--title", f"chore: daily Codex improvements {timestamp}"])
    else:
        sys.exit(test_proc.returncode)


def weekly_run() -> None:
    """Run the weekly full-repo Codex automation."""
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    subprocess.run(["git", "fetch", "origin", "main"], check=False)

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
    prompt = (
        "You are TrendSpire’s deep refactoring and test-generation assistant. Using the full code context below, perform a comprehensive refactor: "
        "1) Add missing pytest tests under tests/\n2) Improve any code smells or inefficiencies\n3) Insert Python logging statements to record function entry/exit and key variables\n4) Update or add docstrings in each function\n5) If new modules or tests are created, include them fully.\n"
        "Output only a unified git diff relative to the repository root.\n\n" + full_code
    )

    prompt_tokens = count_tokens(prompt, WEEKLY_MODEL)
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    try:
        response = openai.Completion.create(engine=WEEKLY_MODEL, prompt=prompt, max_tokens=3000, temperature=0.2)
        diff_response = response.choices[0].text
    except Exception as exc:
        print(f"OpenAI API error: {exc}", file=sys.stderr)
        sys.exit(1)

    completion_tokens = count_tokens(diff_response, WEEKLY_MODEL)
    cost = (prompt_tokens + completion_tokens) * WEEKLY_RATE

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".diff")
    tmp.write(diff_response.encode("utf-8"))
    tmp.close()

    apply_proc = run_cmd(["git", "apply", tmp.name])
    if apply_proc.returncode != 0:
        broken_path = os.path.join(LOG_DIR, f"broken_diff_{timestamp}.diff")
        with open(broken_path, "w", encoding="utf-8") as f:
            f.write(diff_response)
        print(apply_proc.stderr, file=sys.stderr)
        sys.exit(1)

    test_proc = run_cmd(["pytest"])

    summary_path = os.path.join(LOG_DIR, f"summary_{timestamp}_weekly.md")
    snippet = "\n".join(diff_response.splitlines()[:20])
    write_summary(summary_path, WEEKLY_MODEL, "weekly", (prompt_tokens, completion_tokens), cost, test_proc.stdout, snippet)
    append_cost(timestamp, "weekly", (prompt_tokens, completion_tokens), WEEKLY_MODEL, cost)
    log_openai_usage(WEEKLY_MODEL, prompt_tokens, completion_tokens, cost)

    if test_proc.returncode == 0:
        branch = f"codex-weekly-{timestamp}"
        subprocess.run(["git", "checkout", "-b", branch], check=True)
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run(["git", "commit", "-m", f"chore: weekly Codex improvements {timestamp}"], check=True)
        subprocess.run(["git", "push", "origin", branch], check=False)
        run_cmd(["gh", "pr", "create", "--fill", "--title", f"chore: weekly Codex improvements {timestamp}"])
    else:
        sys.exit(test_proc.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Codex automations")
    parser.add_argument("--mode", choices=["daily", "weekly"], required=True)
    args = parser.parse_args()

    load_dotenv()
    ensure_logs()

    if args.mode == "daily":
        daily_run()
    else:
        weekly_run()


if __name__ == "__main__":
    main()
