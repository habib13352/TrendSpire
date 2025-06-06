import json
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

from .fetch_trending import fetch_trending


DEFAULT_CONFIG = {
    "language": "",
    "since": "daily",
    "limit": 10,
}


def load_config() -> dict:
    cfg_path = os.path.join(os.path.dirname(__file__), "config.json")
    if os.path.isfile(cfg_path):
        with open(cfg_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_CONFIG.copy()


def render_trending():
    config = load_config()
    repos = fetch_trending(
        language=config.get("language", ""),
        since=config.get("since", "daily"),
        limit=config.get("limit", 10),
    )

    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))
    template = env.get_template("trending.j2")
    markdown = template.render(
        repos=repos,
        since=config.get("since", "daily"),
        timestamp=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
    )

    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "TRENDING.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)


if __name__ == "__main__":
    render_trending()
