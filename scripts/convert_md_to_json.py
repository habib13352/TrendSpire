import json
import os
import re
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")

REPO_LINE = re.compile(r"\|\s*\[([^\]]+)\]\(([^\)]+)\)\s*\|\s*([0-9,]+)\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|")


def parse_markdown(path: Path):
    """Parse a trending markdown file and return the JSON data."""
    repos = []
    timestamp = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if timestamp is None and line.startswith("_Last updated:"):
            timestamp = line.replace("_Last updated:", "").strip(" _")
        if line.startswith("| ["):
            m = REPO_LINE.match(line)
            if not m:
                continue
            full_name, url, stars, language, description = m.groups()
            try:
                stars_int = int(stars.replace(",", ""))
            except ValueError:
                stars_int = 0
            repos.append({
                "rank": len(repos) + 1,
                "name": full_name,
                "url": url,
                "description": description,
                "language": language,
                "stars": stars_int,
            })
    if not timestamp:
        raise ValueError("Timestamp not found in markdown")
    return {"timestamp": timestamp, "repos": repos}


def convert_file(md_path: Path):
    json_path = md_path.with_suffix(".json")
    if json_path.exists():
        logging.info(f"Skipping {md_path.name} (JSON exists)")
        return
    try:
        data = parse_markdown(md_path)
    except Exception as exc:
        logging.warning(f"Failed to parse {md_path.name}: {exc}")
        return
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    logging.info(f"Converted {md_path.name} -> {json_path.name}")


def main():
    archive_dir = Path(__file__).resolve().parents[1] / "trends" / "archive"
    for md_file in sorted(archive_dir.glob("*.md")):
        convert_file(md_file)


if __name__ == "__main__":
    main()
