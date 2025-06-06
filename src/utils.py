"""Utility functions for TrendSpire scripts."""

from __future__ import annotations

import difflib
import os
import shutil
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

import requests
from openai import OpenAI

LOG_DIR = Path("logs")
BACKUP_DIR = Path("backups")
LOG_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)


def read_file(path: str | Path) -> str:
    """Return the contents of *path* as text."""
    return Path(path).read_text(encoding="utf-8")


def write_file(path: str | Path, content: str) -> None:
    """Write *content* to *path* using UTF-8."""
    Path(path).write_text(content, encoding="utf-8")


def log_update(action: str, details: str) -> None:
    """Append a timestamped log entry describing an update."""
    LOG_DIR.mkdir(exist_ok=True)
    log_path = LOG_DIR / "update_log.txt"
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {action}: {details}\n")


def backup_file(filepath: str | Path) -> Path:
    """Copy *filepath* into ``backups/`` with a timestamp."""
    path = Path(filepath)
    BACKUP_DIR.mkdir(exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    dest = BACKUP_DIR / f"{path.stem}_{timestamp}{path.suffix}"
    shutil.copy2(path, dest)
    return dest


def is_meaningful_change(old_content: str, new_content: str) -> bool:
    """Return ``True`` if two strings differ beyond trivial whitespace."""
    diff = difflib.unified_diff(
        old_content.splitlines(), new_content.splitlines(), lineterm=""
    )
    for line in diff:
        if line.startswith("+") or line.startswith("-"):
            if line.strip() not in {"+", "-"}:
                return True
    return False


def fetch_url(
    url: str,
    *,
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, Any]] = None,
    retries: int = 3,
    backoff: int = 2,
) -> requests.Response:
    """GET ``url`` with retries and exponential backoff."""
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=10)
            resp.raise_for_status()
            return resp
        except Exception as exc:  # pragma: no cover - network errors
            log_update("request_error", f"{url}: {exc}")
            if attempt == retries - 1:
                raise
            time.sleep(backoff ** attempt)
    raise RuntimeError("Unreachable")


def openai_chat(prompt: str, model: str = "gpt-4o", *, retries: int = 3, backoff: int = 2) -> str:
    """Call the OpenAI chat API with retries and return the response text."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    for attempt in range(retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            return resp.choices[0].message.content.strip()
        except Exception as exc:  # pragma: no cover - network errors
            log_update("openai_error", str(exc))
            if attempt == retries - 1:
                raise
            time.sleep(backoff ** attempt)
    raise RuntimeError("Unreachable")


if __name__ == "__main__":
    # Simple examples
    log_update("example", "utilities loaded")
    backup_file("README.md")
    print(is_meaningful_change("a", "b"))
