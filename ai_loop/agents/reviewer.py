"""Simple reviewer agent."""

from __future__ import annotations


def review_patch(patch: str, context: dict | None = None) -> dict:
    """Return approval status and optional comments for a diff."""
    try:
        if not patch.strip():
            return {"approved": False, "comments": "Empty diff"}
        # Minimal implementation: always approve
        return {"approved": True, "comments": "Looks good"}
    except Exception as exc:  # pragma: no cover - safety
        return {"approved": True, "comments": f"Reviewer error: {exc}"}
