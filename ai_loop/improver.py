"""Simplified OpenAI-based code improver.

This module handles prompt formatting and retrieving patch suggestions from
OpenAI. Git operations and patch application will be handled elsewhere.
"""

from __future__ import annotations

import os
from openai import OpenAI, OpenAIError

DEFAULT_MODEL = "gpt-4o"


def format_prompt(diff: str) -> str:
    """Return a basic prompt for the given diff."""
    return f"Suggest improvements for the following diff:\n\n{diff}"


def generate_patch(diff: str, model: str = DEFAULT_MODEL) -> str:
    """Send the prompt to OpenAI and return the raw response."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in environment")
    client = OpenAI(api_key=api_key)
    prompt = format_prompt(diff)
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.choices[0].message.content
    except OpenAIError as exc:
        raise RuntimeError(str(exc)) from exc
