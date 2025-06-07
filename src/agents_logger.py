from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent.parent / "logs" / "agents.log"


def log_agent_action(agent: str, message: str) -> None:
    """Append a timestamped agent log entry."""
    LOG_FILE.parent.mkdir(exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {agent}: {message}\n")
