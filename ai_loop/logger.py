"""Utilities for logging OpenAI usage and prompts."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent / "codex_logs"
LOG_DIR.mkdir(exist_ok=True)

# cost tracking file under memory/
MEMORY_DIR = Path(__file__).resolve().parents[1] / "memory"
COST_TRACKER = MEMORY_DIR / "cost_tracker.csv"
MEMORY_DIR.mkdir(exist_ok=True)


def log_result(
    prompt: str,
    response: str,
    *,
    prompt_tokens: int,
    completion_tokens: int,
    cost: float,
) -> None:
    """Write a log entry and track token costs."""
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    log_path = LOG_DIR / f"log_{timestamp}.txt"
    max_len = 2000

    def _truncate(text: str) -> str:
        return text[:max_len] + ("\n...[truncated]" if len(text) > max_len else "")

    with open(log_path, "w", encoding="utf-8") as fh:
        fh.write(f"timestamp: {timestamp}\n")
        fh.write(f"prompt_tokens: {prompt_tokens}\n")
        fh.write(f"completion_tokens: {completion_tokens}\n")
        fh.write(f"total_cost: {cost:.6f}\n")
        fh.write("prompt:\n")
        fh.write(_truncate(prompt) + "\n")
        fh.write("response:\n")
        fh.write(_truncate(response) + "\n")

    # Append cost tracking row
    write_header = not COST_TRACKER.exists()
    with open(COST_TRACKER, "a", encoding="utf-8") as f:
        if write_header:
            f.write("timestamp,prompt_tokens,completion_tokens,cost_usd\n")
        f.write(f"{timestamp},{prompt_tokens},{completion_tokens},{cost:.6f}\n")
