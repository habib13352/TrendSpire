"""Minimal agent pipeline orchestration."""

from .context_builder import build_context
from .agents import run_planner, run_coder, run_pr_agent


def run() -> str:
    """Execute the Planner → Coder → PR Agent pipeline."""
    print("[AgentLoop] Building context")
    context = build_context()

    plan = run_planner(context)
    diff = run_coder(plan)
    pr_message = run_pr_agent(diff)

    print("[AgentLoop] Pipeline complete")
    print("Phase 2.1 complete: Agent pipeline scaffolded.")
    return pr_message


if __name__ == "__main__":
    run()
