import pathlib


def test_trending_has_entries():
    path = pathlib.Path("TRENDING.md")
    assert path.exists(), "TRENDING.md missing"
    content = path.read_text().splitlines()
    repo_lines = [line for line in content if line.startswith("| [")]
    assert len(repo_lines) >= 5, "Expected at least 5 repositories in TRENDING.md"
