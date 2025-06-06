import json
from pathlib import Path


from .fetch_trending import fetch_trending, render_markdown, TEMPLATE_DIR


DEFAULT_CONFIG = {
    "language": "",
    "since": "daily",
    "limit": 10,
}


def load_config() -> dict:
    """Load trending scraper settings from ``config.json``."""
    cfg_path = Path(__file__).parent / "config.json"
    if cfg_path.is_file():
        return json.loads(cfg_path.read_text(encoding="utf-8"))
    return DEFAULT_CONFIG.copy()


def render_trending() -> str:
    """Generate the trending digest and write ``TRENDING.md``."""
    config = load_config()
    repos = fetch_trending(
        language=config.get("language", ""),
        since=config.get("since", "daily"),
        limit=config.get("limit", 10),
    )

    markdown = render_markdown(repos, config.get("since", "daily"))
    out_path = Path(__file__).resolve().parent.parent / "TRENDING.md"
    out_path.write_text(markdown, encoding="utf-8")
    return markdown


def update_readme(trending_md: str) -> None:
    """Insert the trending digest at the top of README between markers."""
    readme_path = Path(__file__).resolve().parent.parent / "README.md"
    start = "<!-- TRENDING_START -->"
    end = "<!-- TRENDING_END -->"

    content = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

    if start in content and end in content:
        pre, _start, rest = content.partition(start)
        _mid, _end, post = rest.partition(end)
        new_content = pre + start + "\n" + trending_md.strip() + "\n" + end + post
    else:
        new_content = start + "\n" + trending_md.strip() + "\n" + end + "\n" + content

    readme_path.write_text(new_content, encoding="utf-8")


if __name__ == "__main__":
    md = render_trending()
    update_readme(md)
