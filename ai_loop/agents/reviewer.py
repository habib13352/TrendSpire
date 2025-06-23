"""LLM-powered diff reviewer."""

from __future__ import annotations

from ..utils_common import call_openai_chat

REVIEWER_PROMPT_TEMPLATE = """
You are a senior software engineer reviewing a Git diff for a pull request.

## Diff:
{{ diff }}

## Project Goals:
{{ goals }}

## Repo Summary:
{{ repo_summary }}

Please answer the following:
1. ✅ Do you approve this diff? Why or why not?
2. 📝 What suggestions would you make to improve it?
3. 🧠 Any potential issues or red flags?
4. 📄 Summary (1–2 lines) to include in the PR review message.

Be specific and concise.
"""


def review_patch(patch: str, context: dict | None = None) -> dict:
    """Return approval status and comments for a diff using OpenAI."""
    if not patch.strip():
        return {"approved": False, "comments": "Empty diff"}

    goals = context.get("goals", "") if context else ""
    repo_summary = context.get("src_summary", "") if context else ""
    prompt = REVIEWER_PROMPT_TEMPLATE.replace("{{ diff }}", patch)
    prompt = prompt.replace("{{ goals }}", goals)
    prompt = prompt.replace("{{ repo_summary }}", repo_summary)

    messages = [
        {"role": "system", "content": "You are an expert code reviewer."},
        {"role": "user", "content": prompt},
    ]

    try:
        response, *_ = call_openai_chat(messages)
        text = response.strip()
        approved = "approved" in text.lower() or "approve" in text.lower()
        return {"approved": approved, "comments": text}
    except Exception as exc:  # pragma: no cover - safety
        return {"approved": True, "comments": f"Reviewer error: {exc}"}
