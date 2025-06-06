"""Improve markdown files using OpenAI and log usage."""

from __future__ import annotations

import difflib
import os
from datetime import datetime
from pathlib import Path

from openai import OpenAI, OpenAIError

from .api_logger import log_openai_usage

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
RATE = 0.005 / 1000  # cost per token for gpt-4o
LOG_DIR = Path("codex_logs")
COST_LOG = Path("codex_costs.csv")

TRENDING_PROMPT = """You are a GitHub content editor who specializes in trending repositories.\nTake the following raw markdown listing of trending GitHub repositories and rewrite it to be:\n- Clean and well-formatted\n- Engaging and informative\n- Visually appealing using GitHub markdown (headings, lists, emojis)\n- Structured for easy readability\n- Optimized to attract stars and forks\n\nUse sections like:\n- 🔥 Trending Today\n- 🛠️ Developer Tools\n- 📚 Learning Resources\n- 💡 AI & Machine Learning\n- 🌐 Web Dev & Frameworks\n- 🚀 Most Starred of the Day\n\nInput markdown:\n---\n{content}\n---\n\nGive only the improved markdown as output."""

README_PROMPT = """You are a GitHub README.md wizard. Take this basic README and improve it by:\n- Clearly explaining the project purpose\n- Including sections like Features, How it Works, Getting Started, Contributing, and License\n- Adding emojis and section headers for readability\n- Making it appealing to developers and content creators\n\nHere is the original README:\n---\n{content}\n---\n\nReturn only the improved markdown."""


def ensure_logs() -> None:
    """Ensure log directories and cost file exist."""
    LOG_DIR.mkdir(exist_ok=True)
    if not COST_LOG.exists():
        with COST_LOG.open("w", encoding="utf-8") as f:
            f.write(
                "timestamp,run_type,prompt_tokens,completion_tokens,model,cost_usd\n"
            )


def append_cost(run_type: str, tokens: tuple[int, int], model: str, cost: float) -> None:
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    with COST_LOG.open("a", encoding="utf-8") as f:
        f.write(
            f"{timestamp},{run_type},{tokens[0]},{tokens[1]},{model},{cost:.6f}\n"
        )


def call_openai(prompt: str) -> tuple[str, tuple[int, int]]:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    usage = response.usage
    tokens = (usage.prompt_tokens, usage.completion_tokens)
    cost = (tokens[0] + tokens[1]) * RATE
    log_openai_usage(MODEL, tokens[0], tokens[1], cost)
    append_cost("improve", tokens, MODEL, cost)
    return response.choices[0].message.content.strip(), tokens


def write_diff(old: str, new: str, name: str) -> None:
    if old == new:
        return
    diff = difflib.unified_diff(
        old.splitlines(),
        new.splitlines(),
        fromfile=f"{name} before",
        tofile=f"{name} after",
        lineterm="",
    )
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    diff_path = LOG_DIR / f"{name}_{timestamp}.diff"
    diff_path.write_text("\n".join(diff), encoding="utf-8")


def improve_trending(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    prompt = TRENDING_PROMPT.format(content=original)
    try:
        improved, _tokens = call_openai(prompt)
    except OpenAIError as exc:
        print(exc)
        return False
    if improved and improved != original:
        path.write_text(improved + "\n", encoding="utf-8")
        write_diff(original, improved, "trending")
        return True
    return False


def improve_readme(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")
    start = "<!-- TRENDING_START -->"
    end = "<!-- TRENDING_END -->"
    trending_block = ""
    rest = content
    if start in content and end in content:
        pre, _s, tmp = content.partition(start)
        block, _e, post = tmp.partition(end)
        trending_block = start + block + end
        rest = pre + post
    prompt = README_PROMPT.format(content=rest.strip())
    try:
        improved, _tokens = call_openai(prompt)
    except OpenAIError as exc:
        print(exc)
        return False
    new_content = (trending_block + "\n" + improved.strip() + "\n").lstrip()
    if new_content != content:
        path.write_text(new_content, encoding="utf-8")
        write_diff(content, new_content, "readme")
        return True
    return False


def main() -> None:
    ensure_logs()
    changed = False
    trending_path = Path("TRENDING.md")
    if trending_path.exists():
        changed |= improve_trending(trending_path)
    readme_path = Path("README.md")
    if readme_path.exists():
        changed |= improve_readme(readme_path)
    if not changed:
        print("No improvements made.")


if __name__ == "__main__":
    main()
