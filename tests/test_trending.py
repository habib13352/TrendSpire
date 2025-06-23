import pathlib


def test_trending_has_entries():
    path = pathlib.Path("TRENDING.md")
    assert path.exists(), "TRENDING.md missing"
    # ensure UTF-8 decoding so emojis/special chars don't break on Windows
    content = path.read_text(encoding="utf-8").splitlines()
    repo_lines = [line for line in content if line.startswith("| [")]
    assert len(repo_lines) >= 5, "Expected at least 5 repositories in TRENDING.md"
