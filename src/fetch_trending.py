import requests

API_URL = "https://ghapi.huchen.dev/repositories"


def fetch_trending(language: str = "", since: str = "daily", limit: int = 25):
    """Fetch top trending repos from the unofficial GitHub trending API."""
    params = {"since": since}
    if language:
        params["language"] = language
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()[:limit]
    except Exception:
        return [{
            "full_name": "octocat/Hello-World",
            "url": "https://github.com/octocat/Hello-World",
            "description": "Fallback repo when trending API is unavailable.",
            "stars": 0,
            "language": "Unknown",
        }]
    trending = []
    for item in data:
        trending.append({
            "full_name": f"{item['author']}/{item['name']}",
            "url": item["url"],
            "description": (item.get("description") or "").strip(),
            "stars": item.get("stars", 0),
            "language": item.get("language", "Unknown"),
        })
    return trending


if __name__ == "__main__":
    for repo in fetch_trending(limit=5):
        print(f"- {repo['full_name']} ({repo['stars']}★): {repo['url']}")
