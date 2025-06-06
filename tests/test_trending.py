import pathlib
import re


def test_trending_has_entries():
    path = pathlib.Path("TRENDING.md")
    assert path.exists(), "TRENDING.md missing"
    content = path.read_text()
    links = re.findall(r"https://github.com/[\w\-]+/[\w\-]+", content)
    assert len(links) >= 5, "Expected at least 5 repository links in TRENDING.md"
