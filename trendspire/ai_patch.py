"""Generate improved README content using OpenAI."""

import os
import time
import logging
from datetime import datetime, timezone
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from src.openai_helper import ask_openai
from .utils import openai_chat, log_update, load_config


def build_prompt(readme_text: str, config: dict) -> str:
    """Construct the prompt for README rewriting."""
    logo_block = ""
    if config.get("logo_path"):
        logo_block = f"![Logo]({config['logo_path']})"

    contact_section = ""
    if config.get("email"):
        contact_section = f"## Contact\n- Email: {config['email']}"

    extra_sections_md = ""
    for section in config.get("extra_sections", []):
        extra_sections_md += f"## {section['title']}\n{section['content']}\n\n"

    return f"""
You are ChatGPT. Improve the project's README.md with these rules:
1. Insert logo (if provided) at the very top:
   {logo_block}
2. Include any extra sections specified in the config:
   {extra_sections_md}
3. Ensure a “Contact” section with the email is at the bottom:
   {contact_section}
4. Provide a short TL;DR summary and bullet-point suggestions, then output the fully-rewritten README.md.

Here is the current README.md:
{readme_text}
"""

def generate_summary(readme_text: str) -> str:
    """Return a TL;DR summary of the README text."""
    prompt = (
        "You are an AI assistant that reads README files. "
        "Provide a concise TL;DR summary of the following README (2–3 lines):\n\n"
        f"{readme_text}"
    )
    return ask_openai(prompt, temperature=0.3, max_tokens=200)

def suggest_improvements(readme_text: str) -> str:
    """Suggest README improvements using OpenAI."""
    prompt = (
        "You are an expert technical writer. "
        "Suggest specific improvements for this README. "
        "Mention missing sections (Installation, Usage, License, etc.), "
        "clarity of language, badge additions, table of contents, and SEO keywords. "
        "Recommend quick-start examples and other best practices from the Awesome README collection. "
        "Output as bullet points:\n\n"
        f"{readme_text}"
    )
    return ask_openai(prompt, temperature=0.5, max_tokens=400)

def rewrite_readme(readme_text: str, config: dict) -> str:
    """Return a rewritten README using the given config."""
    prompt = build_prompt(readme_text, config)
    return ask_openai(prompt, temperature=0.7, max_tokens=1920)


CODEX_LOG_DIR = Path("codex_logs")
CODEX_LOG_DIR.mkdir(exist_ok=True)


def is_valid_patch(diff: str) -> bool:
    """Return ``True`` if *diff* looks like a valid unified patch."""
    if not diff.strip().startswith("diff --git"):
        return False
    if "@@" not in diff:
        return False
    files: set[str] = set()
    for line in diff.splitlines():
        if line.startswith("diff --git"):
            parts = line.split()
            if len(parts) >= 4:
                for p in parts[2:4]:
                    if p.startswith("a/") or p.startswith("b/"):
                        p = p[2:]
                    if p != "/dev/null":
                        files.add(p)
        elif line.startswith("+++ ") or line.startswith("--- "):
            p = line[4:].strip()
            if p.startswith("a/") or p.startswith("b/"):
                p = p[2:]
            if p != "/dev/null":
                files.add(p)
    return all(os.path.exists(f) for f in files)


def generate_patch(prompt: str, *, attempts: int = 3) -> str:
    """Return a valid patch from OpenAI with retry logic."""
    notes = [
        "",
        "\n\nEnsure @@ headers are included.",
        "\n\nEnsure @@ headers are included. Use valid filenames only.",
    ]
    for i in range(attempts):
        attempt_prompt = prompt + notes[i]
        msg = f"AI patch attempt {i + 1}"
        print(msg)
        logging.info(msg)
        log_update("ai_patch_attempt", msg)
        diff = openai_chat(attempt_prompt)
        if is_valid_patch(diff):
            logging.info("Received valid patch")
            return diff
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        invalid_path = CODEX_LOG_DIR / f"invalid_diff_{timestamp}.txt"
        invalid_path.write_text(diff, encoding="utf-8")
        logging.warning(f"Invalid patch saved to {invalid_path}")
        print(f"Invalid patch saved to {invalid_path}")
        time.sleep(1)
    raise ValueError("Failed to generate valid patch")
