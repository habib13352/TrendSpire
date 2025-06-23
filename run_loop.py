"""Main AI patch cycle runner for TrendSpire."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from ai_loop import context_builder
from ai_loop.agents import run_planner, run_coder, review_patch, pr_agent
from ai_loop.sanity_checker import sanity_check_diff
from ai_loop.utils_common import run_cmd

LOG_DIR = Path("ai_loop/codex_logs")
LOG_DIR.mkdir(exist_ok=True)


def apply_patch(diff: str) -> None:
    """Apply a unified diff using git."""
    patch_path = LOG_DIR / "latest.patch"
    patch_path.write_text(diff, encoding="utf-8")
    run_cmd(["git", "apply", str(patch_path)])


def main() -> None:
    """Execute planner → coder → reviewer → patch workflow."""
    context = context_builder.load_context()
    plan = run_planner(context)
    diff = run_coder(plan, context)

    review = review_patch(diff, context)
    safe, reasons = sanity_check_diff(diff)

    if not safe:
        print("[run_loop] Diff rejected:", "; ".join(reasons))
        return
    if not review.get("approved", True):
        print("[run_loop] Reviewer rejected diff.")
        return

    apply_patch(diff)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    branch = f"ai-patch-{timestamp}"
    run_cmd(["git", "checkout", "-b", branch])
    run_cmd(["git", "add", "-A"])
    run_cmd(["git", "commit", "-m", f"AI patch {timestamp}"])

    pr_message = pr_agent.format_pr(diff)
    (LOG_DIR / f"pr_{timestamp}.md").write_text(pr_message, encoding="utf-8")
    print(pr_message)


if __name__ == "__main__":
    main()
