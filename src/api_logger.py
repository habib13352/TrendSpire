import csv
import logging
import os
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
USAGE_FILE = os.path.join(LOG_DIR, "api_usage.csv")


def ensure_log_dir() -> None:
    """Ensure the log directory and the usage file exist."""
    logging.debug("Ensuring log directory exists at: %s", LOG_DIR)
    os.makedirs(LOG_DIR, exist_ok=True)
    if not os.path.exists(USAGE_FILE):
        with open(USAGE_FILE, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "service",
                "model",
                "prompt_tokens",
                "completion_tokens",
                "cost_usd",
            ])


def log_openai_usage(model: str, prompt_tokens: int, completion_tokens: int, cost: float) -> None:
    """Append an OpenAI API usage entry to the CSV log."""
    logging.debug(
        "Logging OpenAI usage: model=%s, prompt_tokens=%d, completion_tokens=%d, cost=%.6f",
        model,
        prompt_tokens,
        completion_tokens,
        cost,
    )
    ensure_log_dir()
    timestamp = datetime.utcnow().isoformat()
    with open(USAGE_FILE, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            "openai",
            model,
            prompt_tokens,
            completion_tokens,
            f"{cost:.6f}",
        ])
    logging.debug("Logged usage at: %s", timestamp)
