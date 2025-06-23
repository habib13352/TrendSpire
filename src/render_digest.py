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
    """Load the trending scraper configuration from ``config.json``."""
    cfg_path = os.path.join(os.path.dirname(__file__), "config.json")
    if os.path.isfile(cfg_path):
        with open(cfg_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_CONFIG.copy()


def render_trending() -> str:
    """Render the trending digest markdown and write ``TRENDING.md``."""
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

    repo_root = os.path.dirname(os.path.dirname(__file__))
    output_path = os.path.join(repo_root, "TRENDING.md")

    # Archive the previous digest before overwriting
    archive_dir = os.path.join(repo_root, "trends", "archive")
    os.makedirs(archive_dir, exist_ok=True)
    if os.path.isfile(output_path):
        timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        archive_name = f"trending_{timestamp}.md"
        archive_path = os.path.join(archive_dir, archive_name)
        with open(output_path, "r", encoding="utf-8") as src, open(archive_path, "w", encoding="utf-8") as dst:
            dst.write(src.read())

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    return markdown


def update_readme(trending_md: str) -> None:
    """Insert the trending digest at the top of README between markers."""
    repo_root = os.path.dirname(os.path.dirname(__file__))
    readme_path = os.path.join(repo_root, "README.md")
    start = "<!-- TRENDING_START -->"
    end = "<!-- TRENDING_END -->"

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    if start in content and end in content:
        pre, _start, rest = content.partition(start)
        _mid, _end, post = rest.partition(end)
        new_content = pre + start + "\n" + trending_md.strip() + "\n" + end + post
    else:
        new_content = start + "\n" + trending_md.strip() + "\n" + end + "\n" + content

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == "__main__":
    md = render_trending()
    update_readme(md)
