"""Improve README.md using OpenAI and trending data."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import List

from .utils import (
    backup_file,
    is_meaningful_change,
    log_update,
    openai_chat,
    read_file,
    write_file,
)


def extract_trending_summary(path: str | Path = "TRENDING.md") -> str:
    """Return the first three repo lines from ``TRENDING.md``."""
    try:
        content = read_file(path)
    except Exception as exc:  # pragma: no cover - file issues
        log_update("read_error", f"{path}: {exc}")
        return ""

    lines: List[str] = [l for l in content.splitlines() if l.startswith("| [")]
    return "\n".join(lines[:3])


def build_prompt(current_readme: str, trending_summary: str) -> str:
    """Construct the instruction prompt for the language model."""
    return (
        "Improve this README.md. "
        "Make the Features section stronger by including today's top GitHub repos. "
        "Polish the wording and formatting for clarity and appeal.\n\n"
        f"Current README:\n{current_readme}\n\n"
        f"Trending repositories today:\n{trending_summary}\n"
    )


def improve_readme(
    readme_path: str | Path = "README.md",
    trending_path: str | Path = "TRENDING.md",
    *,
    enable: bool = False,
) -> bool:
    """Update README.md in place using OpenAI when *enable* is True."""
    if not enable:
        print("AI README update skipped (use --enable to run)")
        logging.info("README update skipped")
        return False

    try:
        logging.info("Reading current README")
        current = read_file(readme_path)
    except Exception as exc:  # pragma: no cover - file issues
        log_update("read_error", f"{readme_path}: {exc}")
        print(f"Failed to read {readme_path}: {exc}")
        return False

    logging.info("Extracting trending summary")
    summary = extract_trending_summary(trending_path)
    prompt = build_prompt(current, summary)
    logging.info("Sending prompt to OpenAI")

    try:
        improved = openai_chat(prompt)
    except Exception as exc:  # pragma: no cover - network issues
        log_update("openai_failure", str(exc))
        print(f"OpenAI request failed: {exc}")
        return False

    if not is_meaningful_change(current, improved):
        log_update("no_change", "README unchanged after AI step")
        print("README unchanged after AI step")
        return False

    try:
        logging.info("Writing updated README")
        backup_file(readme_path)
        write_file(readme_path, improved + "\n")
        log_update("README updated", "Applied AI improvements to README")
        print("README updated with AI improvements")
        return True
    except Exception as exc:  # pragma: no cover - file issues
        log_update("write_error", f"{readme_path}: {exc}")
        print(f"Failed to write README: {exc}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Improve README with OpenAI")
    parser.add_argument("--enable", action="store_true", help="Run the updater")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    success = improve_readme(enable=args.enable)
    sys.exit(0 if success else 1)
