"""Utility to run a stored prompt through OpenAI Codex and apply the diff."""

from __future__ import annotations

import argparse
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from src.openai_helper import ask_openai


def run(prompt_path: Path, branch: str) -> None:
    prompt_text = prompt_path.read_text(encoding="utf-8")
    diff = ask_openai(prompt_text)

    history_dir = Path("ai_run_history")
    history_dir.mkdir(exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    diff_file = history_dir / f"{prompt_path.stem}_{timestamp}.patch"
    diff_file.write_text(diff, encoding="utf-8")

    patch_path = Path("temp.patch")
    patch_path.write_text(diff, encoding="utf-8")
    subprocess.run(["git", "apply", "--index", str(patch_path)], check=True)

    result = subprocess.run(["pytest", "-q"])
    if result.returncode != 0:
        subprocess.run(["git", "reset", "--hard", "HEAD"], check=True)
        raise SystemExit(result.returncode)

    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
    subprocess.run([
        "git",
        "config",
        "user.email",
        "github-actions[bot]@users.noreply.github.com",
    ], check=True)
    subprocess.run(["git", "checkout", "-b", branch], check=True)
    subprocess.run(["git", "commit", "-am", f"Codex update from {prompt_path.name}"], check=True)
    subprocess.run(["git", "push", "--set-upstream", "origin", branch], check=True)

    # Return to main for subsequent prompts
    subprocess.run(["git", "checkout", "main"], check=True)

    if os.getenv("GITHUB_TOKEN"):
        subprocess.run([
            "gh",
            "pr",
            "create",
            "--title",
            f"Codex update {prompt_path.name}",
            "--body",
            "Automated update via run_prompt.py",
            "--base",
            "main",
        ], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a Codex prompt")
    parser.add_argument("prompt_path", type=Path, help="Path to prompt file")
    parser.add_argument("branch", help="Name of branch to create")
    args = parser.parse_args()
    run(args.prompt_path, args.branch)


if __name__ == "__main__":
    main()
