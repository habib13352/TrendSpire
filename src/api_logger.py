import csv
import json
import logging
import os
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
LOG_FORMAT = os.getenv("API_LOG_FORMAT", "csv").lower()
USAGE_FILE = os.path.join(LOG_DIR, f"api_usage.{LOG_FORMAT}")


def ensure_log_dir() -> None:
    """Ensure the log directory and usage file exist."""
    logging.debug("Ensuring log directory exists at: %s", LOG_DIR)
    os.makedirs(LOG_DIR, exist_ok=True)
    if not os.path.exists(USAGE_FILE):
        logging.debug("Creating usage file %s", USAGE_FILE)
        if LOG_FORMAT == "csv":
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
        elif LOG_FORMAT == "json":
            with open(USAGE_FILE, "w", encoding="utf-8") as f:
                json.dump([], f)
        else:  # txt
            open(USAGE_FILE, "w", encoding="utf-8").close()


def log_openai_usage(model: str, prompt_tokens: int, completion_tokens: int, cost: float) -> None:
    """Append an OpenAI API usage entry in the selected format."""
    logging.debug(
        "Logging OpenAI usage: model=%s, prompt_tokens=%d, completion_tokens=%d, cost=%.6f",
        model,
        prompt_tokens,
        completion_tokens,
        cost,
    )
    ensure_log_dir()
    timestamp = datetime.utcnow().isoformat()
    entry = {
        "timestamp": timestamp,
        "service": "openai",
        "model": model,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "cost_usd": float(f"{cost:.6f}"),
    }
    if LOG_FORMAT == "csv":
        with open(USAGE_FILE, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                entry["timestamp"],
                entry["service"],
                entry["model"],
                entry["prompt_tokens"],
                entry["completion_tokens"],
                entry["cost_usd"],
            ])
    elif LOG_FORMAT == "json":
        with open(USAGE_FILE, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
    else:  # txt
        line = (
            f"{entry['timestamp']} openai {entry['model']} {entry['prompt_tokens']} "
            f"{entry['completion_tokens']} {entry['cost_usd']:.6f}\n"
        )
        with open(USAGE_FILE, "a", encoding="utf-8") as f:
            f.write(line)
    logging.debug("Logged usage at: %s", timestamp)
