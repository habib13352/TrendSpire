"""Improve README.md using OpenAI and trending data."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import List

from utils import (
    backup_file,
    is_meaningful_change,
    log_update,
    openai_chat,
    read_file,
    write_file,
)


def extract_trending_summary(path: str | Path = "TRENDING.md", top_n: int = 3) -> str:
    """Return a short summary of the top trending repositories."""
    try:
        content = read_file(path)
    except Exception as exc:  # pragma: no cover - file issues
        log_update("read_error", f"{path}: {exc}")
        return ""

    lines: List[str] = []
    for line in content.splitlines():
        if line.startswith("| ["):
            lines.append(line)
        if len(lines) >= top_n:
            break
    return "\n".join(lines)


def build_prompt(current_readme: str, trending_summary: str) -> str:
    """Construct the instruction prompt for the language model."""
    return f"""Improve the following README.md by:\n\n- Updating the \"Features\" section with a summary of today's top 3 GitHub trending repositories.\n- Making the README clearer and more appealing using markdown formatting.\n\nCurrent README:\n{current_readme}\n\nTrending repositories today:\n{trending_summary}\n"""


def improve_readme(readme_path: str | Path = "README.md", trending_path: str | Path = "TRENDING.md") -> bool:
    """Update README.md in place using OpenAI if ENABLE_AI_README flag is true."""
    if os.getenv("ENABLE_AI_README", "false").lower() != "true":
        print("AI README update disabled via ENABLE_AI_README flag.")
        return False

    try:
        current = read_file(readme_path)
    except Exception as exc:  # pragma: no cover - file issues
        log_update("read_error", f"{readme_path}: {exc}")
        return False

    summary = extract_trending_summary(trending_path)
    prompt = build_prompt(current, summary)

    try:
        improved = openai_chat(prompt)
    except Exception as exc:  # pragma: no cover - network issues
        log_update("openai_failure", str(exc))
        return False

    if not is_meaningful_change(current, improved):
        log_update("no_change", "README unchanged after AI step")
        return False

    try:
        backup_file(readme_path)
        write_file(readme_path, improved + "\n")
        log_update("README updated", "Applied AI improvements to README")
        return True
    except Exception as exc:  # pragma: no cover - file issues
        log_update("write_error", f"{readme_path}: {exc}")
        return False


if __name__ == "__main__":
    success = improve_readme()
    sys.exit(0 if success else 1)
