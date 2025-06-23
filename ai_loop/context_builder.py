"""Gather high-level repository context for the AI-loop."""

from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MEMORY_FILE = REPO_ROOT / "ai_loop" / "trendspire_memory" / "memory.txt"


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def _summarize(text: str, lines: int = 20) -> str:
    return "\n".join(text.splitlines()[:lines])


def _src_summary() -> str:
    src = REPO_ROOT / "src"
    if not src.is_dir():
        return ""
    names = sorted(p.name for p in src.iterdir())
    return ", ".join(names)


def _latest_trend_summary() -> str:
    archive = REPO_ROOT / "trends" / "archive"
    json_files = list(archive.glob("*.json"))
    if not json_files:
        return ""
    latest = max(json_files)
    try:
        data = json.loads(latest.read_text(encoding="utf-8"))
    except Exception:
        return ""
    parts = [data.get("timestamp", "")]
    for repo in data.get("repos", [])[:5]:
        parts.append(f"{repo.get('name')} ({repo.get('stars')})")
    return "; ".join(parts)


def _memory_excerpt(lines: int = 20) -> str:
    """Return the last few lines of the memory log if present."""
    try:
        return "\n".join(MEMORY_FILE.read_text(encoding="utf-8").splitlines()[-lines:])
    except FileNotFoundError:
        return ""


def load_context() -> dict:
    """Return repository context used for prompting."""
    readme = _read_text(REPO_ROOT / "README.md")
    goals = _read_text(REPO_ROOT / "GOALS.md")
    trending_md = _summarize(_read_text(REPO_ROOT / "TRENDING.md"))
    src_summary = _src_summary()
    trend_json_summary = _latest_trend_summary()
    memory_excerpt = _memory_excerpt()

    context = {
        "readme": readme,
        "src_summary": src_summary,
        "trending_md": trending_md,
        "trend_json_summary": trend_json_summary,
        "goals": goals,
        "memory": memory_excerpt,

    }

    missing = [
        key
        for key in ("goals", "trend_json_summary", "src_summary")
        if not context.get(key)
    ]
    if missing:
        print(f"[ContextBuilder] Warning: missing {', '.join(missing)}")
    else:
        print("[ContextBuilder] Context includes goals, trend snapshot and repo summary")

    return context


# Backwards compatibility
def build_context() -> dict:  # pragma: no cover - legacy alias
    return load_context()
