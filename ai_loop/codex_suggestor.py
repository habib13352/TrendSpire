"""OpenAI helper that turns an improvement idea into a patch diff."""

from __future__ import annotations

import os
from typing import Dict, Tuple

from .logger import log_result
from .utils_common import call_openai_chat

DEFAULT_MODEL = "gpt-4o"
MODEL_PRICES = {"gpt-4o": (0.005, 0.015), "gpt-4": (0.03, 0.06)}


def build_prompt(idea: str, context: Dict[str, str]) -> str:
    parts = [
        "You are an autonomous developer assistant. Respond only with a unified diff.",
        f"\n\n# Goal\n{idea}",
        f"\n\n# README\n{context.get('readme','')}",
        f"\n\n# TRENDING.md\n{context.get('trending_md','')}",
        f"\n\n# Goals\n{context.get('goals','')}",
    ]
    return "\n".join(parts)


def suggest_diff(idea: str, context: Dict[str, str], model: str = DEFAULT_MODEL) -> Tuple[str, Tuple[int, int], float]:
    prompt = build_prompt(idea, context)
    messages = [{"role": "user", "content": prompt}]
    try:
        response, p_tok, c_tok, cost = call_openai_chat(messages, model=model)
        log_result(prompt, response, prompt_tokens=p_tok, completion_tokens=c_tok, cost=cost)
        return response, (p_tok, c_tok), cost
    except Exception as exc:  # pragma: no cover - network failure
        print(f"[codex_suggestor] Failed to get diff: {exc}")
        return "", (0, 0), 0.0
