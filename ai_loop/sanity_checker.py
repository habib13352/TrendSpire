from __future__ import annotations

import os
import re
from typing import List, Tuple

from .utils_common import is_valid_diff, is_suspicious_deletion, call_openai_chat


SYSTEM_PROMPT = (
    "You're a sanity checker for code patches. Given the following diff, "
    "is it safe and valid to apply? Flag any dangerous or suspicious changes."
)


def _llm_safety_check(diff: str) -> list[str]:
    """Optionally ask OpenAI to flag issues. Returns list of concerns."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return []

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": diff},
    ]
    try:
        response, *_ = call_openai_chat(messages)
        text = response.lower()
        if any(word in text for word in ["danger", "suspicious", "malicious"]):
            return [response.strip()]
    except Exception:
        return []
    return []


def sanity_check_diff(diff: str) -> Tuple[bool, List[str]]:
    """Return (is_safe, reasons)."""
    reasons: list[str] = []

    if not diff.strip():
        reasons.append("Diff is empty")
        return False, reasons

    if not is_valid_diff(diff):
        reasons.append("Invalid unified diff format")

    if is_suspicious_deletion(diff):
        reasons.append("Diff deletes entire files")

    dangerous_patterns = [
        r"rm.*-rf",
        r"os\.system\([^\n]*rm.*-rf",
        r"subprocess\.run\([^\n]*rm.*-rf",
    ]
    for pattern in dangerous_patterns:
        if re.search(pattern, diff):
            reasons.append("Contains dangerous command: rm -rf")
            break

    deletions = sum(
        1
        for line in diff.splitlines()
        if line.startswith("-") and not line.startswith("---")
    )
    if deletions > 100:
        reasons.append("Excessive deletions")

    reasons.extend(_llm_safety_check(diff))

    return len(reasons) == 0, reasons
