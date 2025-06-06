"""Fetch GitHub trending repositories and render markdown."""

from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from typing import Any, List

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

from src.utils import backup_file, fetch_url, log_update, write_file

BASE_URL = "https://github.com/trending"
HEADERS = {"User-Agent": "Mozilla/5.0"}

FALLBACK_REPO: dict[str, Any] = {
    "full_name": "octocat/Hello-World",
    "url": "https://github.com/octocat/Hello-World",
    "description": "Fallback repo when scraping fails.",
    "stars": 0,
    "language": "Unknown",
}


class Repo(dict):
    """Container for repository information."""


def fetch_trending(language: str = "", since: str = "daily", limit: int = 25) -> List[Repo]:
    """Return a list of trending repositories from GitHub."""
    url = f"{BASE_URL}/{language}" if language else BASE_URL
    params = {"since": since}
    try:
        resp = fetch_url(url, headers=HEADERS, params=params)
    except Exception as exc:  # pragma: no cover - network errors
        log_update("fetch_error", str(exc))
        return [Repo(**FALLBACK_REPO)]

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
    return repos or [Repo(**FALLBACK_REPO)]


def render_markdown(repos: List[Repo], since: str = "daily") -> str:
    """Render trending markdown using the Jinja template."""
    env = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))
    template = env.get_template("trending.j2")
    return template.render(
        repos=repos,
        since=since,
        timestamp=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
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


def main() -> None:
    """Entry point for running the trending scraper."""
    repos = fetch_trending()
    if repos:
        save_trending(repos)
    else:
        log_update("fetch_empty", "No repositories fetched")


if __name__ == "__main__":
    main()
