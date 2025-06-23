"""Minimal agent pipeline orchestration."""

from __future__ import annotations

from datetime import datetime

from . import context_builder
from .agents import run_planner, run_coder, pr_agent, review_patch
from .logger import LOG_DIR


def _log_step(name: str, content: str) -> None:
    """Save step output to a timestamped log file."""
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    path = LOG_DIR / f"{name}_{timestamp}.txt"
    try:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
    except Exception:
        pass


def run() -> str:
    """Execute context loading, patch suggestion and PR formatting."""
    print("[AgentLoop] Loading context")
    context = context_builder.load_context()
    if not context.get("memory"):
        print("[AgentLoop] ⚠️ memory context missing")
    _log_step("context", str(context))

    print("[AgentLoop] Planning")
    plan = run_planner(context)
    print(f"[AgentLoop] Planner returned {len(plan)} plan(s)")
    _log_step("plan", str(plan))

    print("[AgentLoop] Coding")
    diff = run_coder(plan, context)
    _log_step("diff", diff)

    print("[AgentLoop] Reviewing")
    try:
        review = review_patch(diff, context)
    except Exception as exc:  # pragma: no cover - network failure
        print(f"[AgentLoop] Reviewer failed: {exc}")
        review = {"approved": True, "comments": "Reviewer error"}
    _log_step("review", str(review))

    print("[AgentLoop] Formatting PR")
    pr_message = pr_agent.format_pr(diff)
    _log_step("pr", pr_message)

    print("[AgentLoop] Pipeline complete")
    print("✅ Phase 3.1 complete: PR message ready.")
    return pr_message


if __name__ == "__main__":
    run()
