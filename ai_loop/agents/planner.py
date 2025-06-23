"""Simple planning agent."""

from pathlib import Path


GOALS_FILE = Path(__file__).resolve().parents[2] / "GOALS.md"


def run(context: dict | None = None) -> list[str]:
    """Return a list of planned steps based on GOALS.md and context."""
    print("[Planner] Reading project goals...")
    try:
        goals_text = GOALS_FILE.read_text(encoding="utf-8")
    except FileNotFoundError:
        goals_text = ""
    print("[Planner] Creating simple plan from goals and context")
    plan = [
        "Read repository context",
        "Call coder agent to draft a patch",
        "Format pull request message",
    ]
    if context:
        plan.append("Context size: " + str(len(context.get('readme', ''))))
    return plan
