"""OpenAI prompt generation and request helpers."""

from __future__ import annotations

import os
from openai import OpenAI, OpenAIError

from .logger import log_result

DEFAULT_MODEL = "gpt-4o"
MODEL_PRICES = {
    "gpt-4o": (0.005, 0.015),  # prompt, completion per 1K tokens
    "gpt-4": (0.03, 0.06),
}


def create_prompt(context: dict) -> str:
    """Format repository context into a single prompt string."""
    sections = [
        "You are an autonomous developer assistant. "
        "Suggest one small improvement to the repository below. "
        "Respond only with a unified diff.",
        "\n\n# README\n" + context.get("readme", ""),
        "\n\n# Source Summary\n" + context.get("src_summary", ""),
        "\n\n# Trending Digest\n" + context.get("trending_md", ""),
        "\n\n# Latest Trend Snapshot\n" + context.get("trend_json_summary", ""),
        "\n\n# Goals\n" + context.get("goals", ""),
    ]
    return "\n".join(sections)


def request_suggestion(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """Send the prompt to OpenAI and return the diff text."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in environment")

    client = OpenAI(api_key=api_key)
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
    except OpenAIError as exc:
        raise RuntimeError(str(exc)) from exc

    content = resp.choices[0].message.content
    usage = resp.usage
    prompt_tokens = getattr(usage, "prompt_tokens", 0)
    completion_tokens = getattr(usage, "completion_tokens", 0)
    price = MODEL_PRICES.get(model, (0.0, 0.0))
    cost = (prompt_tokens / 1000 * price[0]) + (completion_tokens / 1000 * price[1])

    log_result(
        prompt,
        content,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        cost=cost,
    )

    return content


def suggest_patch(context: dict, model: str = DEFAULT_MODEL) -> str:
    """High-level helper that builds the prompt and returns the diff."""
    prompt = create_prompt(context)
    return request_suggestion(prompt, model=model)
