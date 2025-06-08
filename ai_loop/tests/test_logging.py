import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root))

from ai_loop.utils_common import ensure_logs


def test_ensure_logs_creates_files(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    ensure_logs('logs', 'costs.csv', 'mem')

    assert (tmp_path / 'logs').is_dir()
    assert (tmp_path / 'mem').is_dir()
    assert (tmp_path / 'costs.csv').is_file()
