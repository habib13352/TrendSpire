"""Minimal agent pipeline orchestration."""

from . import context_builder
from .agents import run_planner, run_coder, pr_agent


def run() -> str:
    """Execute context loading, patch suggestion and PR formatting."""
    print("[AgentLoop] Loading context")
    context = context_builder.load_context()

    print("[AgentLoop] Planning")
    plan = run_planner(context)

    print("[AgentLoop] Coding")
    diff = run_coder(plan, context)

    print("[AgentLoop] Formatting PR")
    pr_message = pr_agent.format_pr(diff)

    print("[AgentLoop] Pipeline complete")
    print("✅ Phase 2.3 complete: PR message ready.")
    return pr_message


if __name__ == "__main__":
    run()
