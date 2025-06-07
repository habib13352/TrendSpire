import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

import trendspire.ai_patch as ai_patch


def test_is_valid_patch(tmp_path, monkeypatch):
    file1 = tmp_path / "file.py"
    file1.write_text("print('hi')\n")
    monkeypatch.chdir(tmp_path)
    diff = (
        "diff --git a/file.py b/file.py\n"
        "--- a/file.py\n"
        "+++ b/file.py\n"
        "@@\n"
        "-print('hi')\n"
        "+print('bye')\n"
    )
    assert ai_patch.is_valid_patch(diff)


def test_generate_patch_retries(tmp_path, monkeypatch):
    file1 = tmp_path / "file.py"
    file1.write_text("print('hi')\n")
    monkeypatch.chdir(tmp_path)

    attempts = []
    def fake_chat(prompt):
        attempts.append(prompt)
        if len(attempts) == 1:
            return "invalid"
        return (
            "diff --git a/file.py b/file.py\n"
            "--- a/file.py\n"
            "+++ b/file.py\n"
            "@@\n"
            "-print('hi')\n"
            "+print('bye')\n"
        )

    monkeypatch.setattr(ai_patch, "openai_chat", fake_chat)
    monkeypatch.setattr(ai_patch, "CODEX_LOG_DIR", tmp_path / "logs")

    patch = ai_patch.generate_patch("prompt", attempts=2)
    assert patch.startswith("diff --git")
    invalid_files = list((tmp_path / "logs").glob("invalid_diff_*.txt"))
    assert len(invalid_files) == 1
