"""Generate a simple improvement idea from repository context."""

from __future__ import annotations

from typing import Dict


def generate_idea(context: Dict[str, str] | None = None) -> str:
    """Return a short improvement idea based on GOALS.md or fallback."""
    if not context:
        context = {}

    goals = context.get("goals", "")
    for line in goals.splitlines():
        stripped = line.strip()
        if stripped.startswith("-") and len(stripped) > 1:
            # Use the first bullet point as an idea
            return stripped.lstrip("- ")

    trending = context.get("trending_md", "")
    if trending:
        return "Update TRENDING.md formatting"

    return "General code cleanup"
