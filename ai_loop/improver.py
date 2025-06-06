"""Generate improved README content using OpenAI."""

import os
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

from src.openai_helper import ask_openai


def load_config(path: str | Path = "config.yaml") -> dict:
    """Load configuration YAML if present."""
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


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
