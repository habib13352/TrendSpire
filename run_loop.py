"""Run a full AI improvement cycle for TrendSpire."""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path

from ai_loop import context_builder
from ai_loop import improver
from ai_loop import codex_suggestor
from ai_loop import patch_applier
from ai_loop.agents import pr_agent
from ai_loop.sanity_checker import sanity_check_diff
from ai_loop.utils_common import run_cmd

LOG_DIR = Path("ai_loop/codex_logs")
LOG_DIR.mkdir(exist_ok=True)
PATCH_HISTORY = Path("memory/patch_history.json")


def log_history(entry: dict) -> None:
    history = []
    if PATCH_HISTORY.exists():
        try:
            history = json.loads(PATCH_HISTORY.read_text(encoding="utf-8"))
        except Exception:
            history = []
    history.append(entry)
    PATCH_HISTORY.write_text(json.dumps(history, indent=2), encoding="utf-8")


def main() -> None:
    """Execute idea generation, diff creation and PR submission."""
    context = context_builder.load_context()
    idea = improver.generate_idea(context)
    print(f"[run_loop] Idea: {idea}")

    diff, tokens, cost = codex_suggestor.suggest_diff(idea, context)
    if not diff.strip():
        print("[run_loop] No diff returned")
        return
    print(f"[run_loop] Diff size: {len(diff.splitlines())} lines")

    safe, reasons = sanity_check_diff(diff)
    if not safe:
        print("[run_loop] Diff rejected:", "; ".join(reasons))
        return

    patch_file = patch_applier.apply_patch(diff)
    print(f"[run_loop] Patch applied via {patch_file}")

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    branch = f"ai-patch-{timestamp}"
    run_cmd(["git", "checkout", "-b", branch])
    run_cmd(["git", "add", "-A"])
    commit_msg = f"🤖 AI Patch: {idea}"
    run_cmd(["git", "commit", "-m", commit_msg])
    try:
        run_cmd(["git", "push", "--set-upstream", "origin", branch])
    except Exception as exc:
        print(f"[run_loop] Push failed: {exc}")
        return

    pr_body = pr_agent.format_pr(diff)
    (LOG_DIR / f"pr_{timestamp}.md").write_text(pr_body, encoding="utf-8")
    try:
        result = run_cmd([
            "gh",
            "pr",
            "create",
            "--title",
            commit_msg,
            "--body",
            pr_body,
            "--head",
            branch,
            "--base",
            "main",
        ])
        pr_url = result.stdout.strip().splitlines()[-1]
    except Exception as exc:
        print(f"[run_loop] PR creation failed: {exc}")
        pr_url = ""

    log_history({
        "timestamp": timestamp,
        "branch": branch,
        "idea": idea,
        "pr_url": pr_url,
        "tokens": tokens,
        "cost": cost,
    })
    print(f"[run_loop] PR URL: {pr_url}")


if __name__ == "__main__":
    main()
