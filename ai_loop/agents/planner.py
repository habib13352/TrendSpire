"""Simple planning agent placeholder."""

from pathlib import Path


GOALS_FILE = Path(__file__).resolve().parents[2] / "GOALS.md"


def run(context: dict | None = None) -> list[str]:
    """Return a list of planned steps based on GOALS.md."""
    print("[Planner] Reading project goals...")
    try:
        goals_text = GOALS_FILE.read_text(encoding="utf-8")
    except FileNotFoundError:
        goals_text = ""
    print("[Planner] Creating simple plan from goals")
    # Very naive parsing: extract headings under PHASED ROADMAP
    plan = [
        "Review GOALS.md for roadmap",
        "Generate code changes based on roadmap",
        "Prepare pull request",
    ]
    return plan
