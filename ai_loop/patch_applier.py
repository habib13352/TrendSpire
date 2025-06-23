"""Utility to apply unified diffs using git."""

from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone

from .utils_common import run_cmd

LOG_DIR = Path("ai_loop/codex_logs")
LOG_DIR.mkdir(exist_ok=True)


def apply_patch(diff: str) -> Path:
    """Write *diff* to a patch file and apply it with git."""
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    patch_path = LOG_DIR / f"patch_{timestamp}.patch"
    patch_path.write_text(diff, encoding="utf-8")
    run_cmd(["git", "apply", str(patch_path)])
    return patch_path
