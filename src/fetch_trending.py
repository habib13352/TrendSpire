"""Fetch the list of trending repositories from GitHub."""

from pathlib import Path
import sys
from bs4 import BeautifulSoup

# Ensure project root is on ``sys.path`` when executed directly
sys.path.append(str(Path(__file__).resolve().parents[1]))

from typing import Any

from utils import fetch_url, log_update


BASE_URL = "https://github.com/trending"
HEADERS = {"User-Agent": "Mozilla/5.0"}

FALLBACK_REPO = {
    "full_name": "octocat/Hello-World",
    "url": "https://github.com/octocat/Hello-World",
    "description": "Fallback repo when trending scraping fails.",
    "stars": 0,
    "language": "Unknown",
}


def fetch_trending(language: str = "", since: str = "daily", limit: int = 25) -> list[dict[str, Any]]:
    """Return trending repositories for the given language, period and limit."""
    url = BASE_URL
    if language:
        url = f"{BASE_URL}/{language}"
    params = {"since": since}

    try:
        response = fetch_url(url, params=params, headers=HEADERS)
    except Exception as exc:
        log_update("fetch_error", str(exc))
        return [FALLBACK_REPO]

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="Box-row")

    trending = []
    for item in articles[:limit]:
        repo_link_tag = item.h2.a
        repo_path = repo_link_tag["href"].strip()
        full_name = repo_path.lstrip("/")
        repo_url = f"https://github.com{repo_path}"

        desc_tag = item.find("p")
        description = desc_tag.text.strip() if desc_tag else ""

        star_tag = item.find("a", href=lambda s: s and s.endswith("/stargazers"))
        stars = 0
        if star_tag:
            star_text = star_tag.text.strip().replace(",", "")
            try:
                stars = int(star_text)
            except ValueError:
                stars = 0

        lang_tag = item.find("span", attrs={"itemprop": "programmingLanguage"})
        language_text = lang_tag.text.strip() if lang_tag else "Unknown"

        trending.append({
            "full_name": full_name,
            "url": repo_url,
            "description": description,
            "stars": stars,
            "language": language_text,
        })

    if not trending:
        trending = [FALLBACK_REPO]

    return trending


if __name__ == "__main__":
    for repo in fetch_trending(limit=5):
        print(f"- {repo['full_name']} ({repo['stars']}★): {repo['url']}")
