from pathlib import Path

from ai_loop import context_builder


def test_load_context_missing_memory(tmp_path, monkeypatch):
    repo = tmp_path
    monkeypatch.setattr(context_builder, "REPO_ROOT", repo)
    monkeypatch.setattr(context_builder, "MEMORY_FILE", repo / "ai_loop/trendspire_memory/memory.txt")

    (repo / "README.md").write_text("r")
    (repo / "GOALS.md").write_text("g")
    (repo / "TRENDING.md").write_text("t")
    (repo / "trends/archive").mkdir(parents=True)

    ctx = context_builder.load_context()
    assert ctx["memory"] == ""


def test_load_context_with_memory(tmp_path, monkeypatch):
    repo = tmp_path
    memory_file = repo / "ai_loop/trendspire_memory/memory.txt"
    memory_file.parent.mkdir(parents=True)
    memory_file.write_text("line1\nline2")

    monkeypatch.setattr(context_builder, "REPO_ROOT", repo)
    monkeypatch.setattr(context_builder, "MEMORY_FILE", memory_file)

    (repo / "README.md").write_text("r")
    (repo / "GOALS.md").write_text("g")
    (repo / "TRENDING.md").write_text("t")
    (repo / "trends/archive").mkdir(parents=True)

    ctx = context_builder.load_context()
    assert "line2" in ctx["memory"]

