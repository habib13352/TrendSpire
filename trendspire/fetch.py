"""Fetch GitHub trending repositories and render markdown digests."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from dataclasses import dataclass
from typing import List

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

from .utils import backup_file, fetch_url, log_update, write_file, load_config as load_yaml_config

BASE_URL = "https://github.com/trending"
REQUEST_HEADERS = {"User-Agent": "Mozilla/5.0"}
TEMPLATE_DIR = Path(__file__).parent / "templates"


@dataclass
class Repo:
    """Container for repository information."""

    full_name: str
    url: str
    description: str
    stars: int
    language: str


FALLBACK_REPO = Repo(
    full_name="octocat/Hello-World",
    url="https://github.com/octocat/Hello-World",
    description="Fallback repo when scraping fails.",
    stars=0,
    language="Unknown",
)


def fetch_trending(language: str = "", since: str = "daily", limit: int = 25) -> List[Repo]:
    """Return a list of trending repositories from GitHub."""
    url = f"{BASE_URL}/{language}" if language else BASE_URL
    params = {"since": since}
    try:
        resp = fetch_url(url, headers=REQUEST_HEADERS, params=params)
    except Exception as exc:  # pragma: no cover - network errors
        log_update("fetch_error", str(exc))
        return [FALLBACK_REPO]

    soup = BeautifulSoup(resp.text, "html.parser")
    repos: List[Repo] = []
    for item in soup.find_all("article", class_="Box-row")[:limit]:
        repo_path = item.h2.a["href"].strip()
        desc_tag = item.find("p")
        star_tag = item.find("a", href=lambda s: s and s.endswith("/stargazers"))
        lang_tag = item.find("span", attrs={"itemprop": "programmingLanguage"})
        try:
            stars = int((star_tag.text.strip().replace(",", "")) if star_tag else "0")
        except ValueError:
            stars = 0
        repos.append(
            Repo(
                full_name=repo_path.lstrip("/"),
                url=f"https://github.com{repo_path}",
                description=desc_tag.text.strip() if desc_tag else "",
                stars=stars,
                language=lang_tag.text.strip() if lang_tag else "Unknown",
            )
        )
    return repos or [FALLBACK_REPO]


def render_markdown(repos: List[Repo], since: str = "daily") -> str:
    """Render trending markdown using the Jinja template."""
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("trending.j2")
    return template.render(
        repos=repos,
        since=since,
        timestamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    )


def save_trending(repos: List[Repo], path: str | Path = "TRENDING.md", since: str = "daily") -> None:
    """Write trending repositories to *path* in markdown format."""
    markdown = render_markdown(repos, since)
    try:
        backup_file(path)
        write_file(path, markdown)
        log_update("TRENDING updated", f"Saved {len(repos)} repositories")
    except Exception as exc:  # pragma: no cover - file errors
        log_update("write_error", f"{path}: {exc}")


DEFAULT_CONFIG = {
    "language": "",
    "since": "daily",
    "limit": 10,
}


def load_config(path: str | Path = "config.yaml") -> dict:
    """Return merged configuration from YAML with defaults."""
    cfg = DEFAULT_CONFIG.copy()
    cfg.update(load_yaml_config(path))
    return cfg


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


def main() -> None:
    """Entry point for running the trending scraper."""
    repos = fetch_trending()
    if repos:
        save_trending(repos)
    else:
        log_update("fetch_empty", "No repositories fetched")


if __name__ == "__main__":
    main()
