"""Fetch the list of trending repositories from GitHub."""

import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)


BASE_URL = "https://github.com/trending"
HEADERS = {"User-Agent": "Mozilla/5.0"}

FALLBACK_REPO = {
    "full_name": "octocat/Hello-World",
    "url": "https://github.com/octocat/Hello-World",
    "description": "Fallback repo when trending scraping fails.",
    "stars": 0,
    "language": "Unknown",
}


def fetch_trending(language: str = "", since: str = "daily", limit: int = 25):
    """Scrape GitHub Trending for a list of repositories."""
    logging.debug(
        "Fetching trending repositories: language=%s, since=%s, limit=%d",
        language,
        since,
        limit,
    )
    url = BASE_URL
    if language:
        url = f"{BASE_URL}/{language}"
    params = {"since": since}

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        logging.debug("Trending request URL: %s", response.url)
        response.raise_for_status()
    except Exception as e:
        logging.warning("Failed to fetch trending repos: %s", e)
        return [FALLBACK_REPO]

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="Box-row")

    trending = []
    for item in articles[:limit]:
        logging.debug("Processing trending repository article")
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

    logging.debug("Fetched %d trending repositories", len(trending))
    return trending


if __name__ == "__main__":
    for repo in fetch_trending(limit=5):
        print(f"- {repo['full_name']} ({repo['stars']}★): {repo['url']}")
