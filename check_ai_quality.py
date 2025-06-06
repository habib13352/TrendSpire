"""Validate AI-generated README quality."""
from __future__ import annotations

import os
from pathlib import Path
import markdown
from utils import log_update

REQUIRED_SECTIONS = ["features", "usage", "installation"]


def check_readme(readme_path: str | Path = "README.md") -> tuple[bool, str]:
    content = Path(readme_path).read_text(encoding="utf-8")
    try:
        markdown.markdown(content)
    except Exception as exc:
        return False, f"Markdown error: {exc}"
    lower = content.lower()
    for sec in REQUIRED_SECTIONS:
        if f"# {sec}" not in lower:
            return False, f"Missing section: {sec.title()}"
    return True, "README looks good"


def main() -> None:
    ok, message = check_readme()
    log_update("readme_quality", message)
    if not ok:
        token = os.environ.get("GITHUB_TOKEN")
        repo = os.environ.get("GITHUB_REPOSITORY")
        if token and repo:
            import requests
            url = f"https://api.github.com/repos/{repo}/issues"
            requests.post(url, headers={"Authorization": f"token {token}"}, json={"title": "README quality issue", "body": message})
    print(message)

if __name__ == "__main__":
    main()
