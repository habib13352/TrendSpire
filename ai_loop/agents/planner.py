"""Simple planning agent with lightweight reasoning."""

from __future__ import annotations

from pathlib import Path


GOALS_FILE = Path(__file__).resolve().parents[2] / "GOALS.md"


def _base_plan(target: str) -> list[str]:
    return [
        f"Review {target} for possible improvements",
        "Call coder agent to draft a patch",
        "Format pull request message",
    ]


def run(context: dict | None = None) -> list[list[str]]:
    """Return multiple plan options based on GOALS.md and context."""
    print("[Planner] Reading project goals...")
    try:
        goals_text = GOALS_FILE.read_text(encoding="utf-8")
    except FileNotFoundError:
        goals_text = ""

    print("[Planner] Creating plan options")

    src_files: list[str] = []
    if context:
        src_summary = context.get("src_summary", "")
        if src_summary:
            src_files = [p.strip() for p in src_summary.split(",") if p.strip()]

    primary = src_files[0] if src_files else "README.md"
    plans = [_base_plan(primary)]

    # Alternate plan references tests and docs for broader coverage
    alt_plan = [
        "Check ai_loop/tests for missing coverage",
        f"Update documentation referencing {primary}",
        "Call coder agent to draft a patch",
    ]
    plans.append(alt_plan)

    if "Phase 3" in goals_text:
        plans.append([
            "Implement Phase 3 tasks described in GOALS.md",
            "Run coder agent to apply sanity checks",
            "Update project roadmap",
        ])

    return plans
