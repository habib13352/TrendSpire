"""Minimal agent pipeline orchestration."""

from __future__ import annotations
from datetime import datetime, timezone
import json

from . import context_builder
from .context_builder import MEMORY_CONTEXT
from .agents import run_planner, run_coder, pr_agent, review_patch
from .sanity_checker import sanity_check_diff
from .logger import LOG_DIR


def _log_step(name: str, content: str) -> None:
    """Save step output to a timestamped log file."""
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    path = LOG_DIR / f"{name}_{timestamp}.txt"
    try:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
    except Exception:
        pass  # Logging is non-blocking


def _load_saved_memory() -> dict:
    """Return structured memory context if available."""
    if not MEMORY_CONTEXT.exists():
        return {}

    try:
        data = json.loads(MEMORY_CONTEXT.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"[AgentLoop] ⚠️ memory context malformed")
        return {}

    print(f"[AgentLoop] Loaded memory from {MEMORY_CONTEXT}")
    return data


def run() -> str:
    """Execute context loading, patch suggestion and PR formatting."""
    print("[AgentLoop] Loading context")
    context = context_builder.load_context()
    memory_json = _load_saved_memory()
    if memory_json:
        context["memory_json"] = memory_json
    else:
        print(f"[AgentLoop] ⚠️ memory context missing ({MEMORY_CONTEXT} not found)")
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
    except Exception as exc:
        print(f"[AgentLoop] Reviewer failed: {exc}")
        review = {"approved": True, "comments": "Reviewer error"}
    print(f"[Reviewer] Approved: {review.get('approved')}\n[Reviewer] Comments: {review.get('comments')}")
    _log_step("review", str(review))

    print("[AgentLoop] Sanity checking")
    is_safe, reasons = sanity_check_diff(diff)
    _log_step("sanity", str({"safe": is_safe, "reasons": reasons}))

    if not is_safe:
        message = "Sanity check failed: " + "; ".join(reasons)
        print(f"[AgentLoop] ❌ {message}")
        return message
    else:
        print("[AgentLoop] ✅ Sanity check passed: Diff is safe and valid.")
        if reasons:
            print("[AgentLoop] ℹ️ Sanity notes: " + "; ".join(reasons))

    print("[AgentLoop] Formatting PR")
    pr_message = pr_agent.format_pr(diff)
    if review.get("comments"):
        pr_message += "\n\n### Reviewer Summary\n" + review["comments"]
    _log_step("pr", pr_message)

    print("[AgentLoop] Pipeline complete")
    print("✅ Phase 3.2 complete: PR message ready.")
    return pr_message


if __name__ == "__main__":
    run()
