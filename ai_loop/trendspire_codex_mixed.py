#!/usr/bin/env python3
"""Automation orchestrator for TrendSpire Codex workflows."""

import argparse
import os
import re
import subprocess
import sys
import tempfile
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
    append_cost,
    write_summary,
    load_prompt,
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


def get_analysis_prompt(file_path: str, code: str) -> str:
    template = load_prompt("per_file.j2")
    return template.replace("{{ file_path }}", file_path).replace("{{ code }}", code)


def verify_and_finalize_prompt(original_code: str, suggested_code: str) -> str:
    return f"""You previously reviewed this code:

Original:
```python
{original_code}
```
Suggested Rewrite:
```python
{suggested_code}
```
✅ Please double-check the rewritten code.

Does it preserve original functionality?

Are the improvements meaningful?

Is it production-safe and PEP8 compliant?

Return ONLY the finalized updated version.
"""


def get_pr_message_prompt(suggestions_summary: str, file_list: list[str]) -> str:
    files = '\n'.join(f"- `{f}`" for f in file_list)
    return f"""You are a GitHub assistant preparing an automated Pull Request.

📝 TASK:
Summarize the improvements made across these files:
{files}

💡 Use this suggestion summary as context:
{suggestions_summary}

Please write a clear:
1. PR Title
2. PR Body
(Include why the change matters, any risks, and that it was auto-generated)

Format:
Title: <your title here>
Body:
<your detailed PR message here>
"""


def get_log_summary_prompt(file_path: str, issues: str, new_code: str) -> str:
    return f"""You are a GitHub automation logger.

Please create a compact summary for today's automated suggestion for:
📄 File: `{file_path}`

🪲 Issues Identified:
{issues}

✅ Rewritten Code:
```python
{new_code}
```
📦 Format the summary in plain markdown for a changelog file or commit message.
"""


def extract_code_block(text: str) -> str:
    match = re.search(r"```python\n(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_summary(text: str) -> str:
    code_match = re.search(r"```python\n.*?```", text, re.DOTALL)
    if code_match:
        return text[: code_match.start()].strip()
    return text.strip()


def get_target_files(root: str):
    for r, _dirs, names in os.walk(root):
        for name in names:
            if name.endswith(".py"):
                yield os.path.join(r, name)


def mixed_run() -> None:
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    branch = f"codex-mixed-{timestamp}"
    subprocess.run(["git", "checkout", "-b", branch], check=True)

    summaries: list[str] = []
    changed_files: list[str] = []

    for path in get_target_files(SOURCE_DIR):
        with open(path, "r", encoding="utf-8") as f:
            original_code = f.read()

        prompt = get_analysis_prompt(path, original_code)
        try:
            response = client.chat.completions.create(
                model=WEEKLY_MODEL,
                messages=[{"role": "user", "content": prompt}],
            )
            analysis_text = response.choices[0].message.content
        except OpenAIError as exc:
            print(exc, file=sys.stderr)
            continue

        new_code = extract_code_block(analysis_text)
        summary = extract_summary(analysis_text)

        if new_code and new_code != original_code:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_code)
            changed_files.append(path)
            summaries.append(summary)

            log_path = os.path.join(LOG_DIR, f"mixed_{timestamp}.md")
            with open(log_path, "a", encoding="utf-8") as logf:
                logf.write(get_log_summary_prompt(path, summary, new_code))
                logf.write("\n")

    if not changed_files:
        print("No changes produced", file=sys.stderr)
        return

    try:
        run_cmd(["pytest"])
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return

    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(
        ["git", "commit", "-m", f"chore: codex mixed improvements {timestamp}"],
        check=True,
    )
    subprocess.run(["git", "push", "origin", branch], check=False)

    pr_prompt = get_pr_message_prompt("\n".join(summaries), changed_files)
    try:
        pr_resp = client.chat.completions.create(
            model=DAILY_MODEL,
            messages=[{"role": "user", "content": pr_prompt}],
        )
        pr_text = pr_resp.choices[0].message.content
    except OpenAIError as exc:
        print(exc, file=sys.stderr)
        return

    title = "Codex Improvements"
    body = pr_text.strip()
    for line in pr_text.splitlines():
        if line.lower().startswith("title:"):
            title = line.split("Title:", 1)[1].strip()
        elif line.lower().startswith("body:"):
            body = pr_text.split("Body:", 1)[1].strip()
            break

    run_cmd(["gh", "pr", "create", "--title", title, "--body", body])


def daily_run() -> None:
    """Run the daily diff-based Codex automation."""
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    subprocess.run(["git", "fetch", "origin", "main"], check=False)

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
    template = load_prompt("weekly.refactor.j2")
    prompt = template.replace("{{ review_context }}", "").replace(
        "{{ full_code }}", full_code
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
        subprocess.run(["git", "checkout", "-b", branch], check=True)
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run(["git", "commit", "-m", f"chore: weekly Codex improvements {timestamp}"], check=True)
        subprocess.run(["git", "push", "origin", branch], check=False)
        run_cmd(["gh", "pr", "create", "--fill", "--title", f"chore: weekly Codex improvements {timestamp}"])
    else:
        sys.exit(test_proc.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Codex automations")
    parser.add_argument(
        "--mode",
        choices=["daily", "weekly", "mixed"],
        required=True,
        help=(
            "Choose 'daily' for diff-only runs, 'weekly' for full-repo runs, or '"
            "mixed' for per-file analysis"
        ),
    )
    args = parser.parse_args()
    ensure_logs(LOG_DIR, COST_LOG)

    if args.mode == "daily":
        daily_run()
    elif args.mode == "weekly":
        weekly_run()
    else:
        mixed_run()


if __name__ == "__main__":
    main()
