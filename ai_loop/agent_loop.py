"""Minimal agent pipeline orchestration."""

from . import context_builder, suggestor
from .agents import pr_agent


def run() -> str:
    """Execute context loading, patch suggestion and PR formatting."""
    print("[AgentLoop] Loading context")
    context = context_builder.load_context()

    print("[AgentLoop] Requesting patch suggestion")
    diff = suggestor.suggest_patch(context)

    print("[AgentLoop] Formatting PR")
    pr_message = pr_agent.format_pr(diff)

    print("[AgentLoop] Pipeline complete")
    print("✅ Phase 2.2 complete: AI suggestion generated.")
    return pr_message


if __name__ == "__main__":
    run()
