"""Fetch GitHub trending repos and update TRENDING.md."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import List

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

from utils import backup_file, fetch_url, log_update, write_file

BASE_URL = "https://github.com/trending"
HEADERS = {"User-Agent": "Mozilla/5.0"}


class Repo(dict):
    """Simple container for repository info."""


def fetch_trending(language: str = "", since: str = "daily", limit: int = 10) -> List[Repo]:
    """Return a list of trending repositories from GitHub."""
    url = f"{BASE_URL}/{language}" if language else BASE_URL
    params = {"since": since}
    try:
        resp = fetch_url(url, headers=HEADERS, params=params)
    except Exception as exc:  # pragma: no cover - network errors
        log_update("fetch_error", str(exc))
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    repos: List[Repo] = []
    for item in soup.find_all("article", class_="Box-row")[:limit]:
        repo_path = item.h2.a["href"].strip()
        full_name = repo_path.lstrip("/")
        desc_tag = item.find("p")
        description = desc_tag.text.strip() if desc_tag else ""
        star_tag = item.find("a", href=lambda s: s and s.endswith("/stargazers"))
        star_text = star_tag.text.strip().replace(",", "") if star_tag else "0"
        try:
            stars = int(star_text)
        except ValueError:
            stars = 0
        lang_tag = item.find("span", attrs={"itemprop": "programmingLanguage"})
        language_text = lang_tag.text.strip() if lang_tag else "Unknown"
        repos.append(
            Repo(
                full_name=full_name,
                url=f"https://github.com{repo_path}",
                description=description,
                stars=stars,
                language=language_text,
            )
        )
    return repos


def render_markdown(repos: List[Repo], since: str = "daily") -> str:
    """Render the trending markdown using the Jinja template."""
    env = Environment(loader=FileSystemLoader("src/templates"))
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
    repos = fetch_trending()
    if repos:
        save_trending(repos)
    else:
        log_update("fetch_empty", "No repositories fetched")


if __name__ == "__main__":
    main()
