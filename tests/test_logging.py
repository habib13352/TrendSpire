import os
import sys
import importlib.util
from pathlib import Path


def test_ensure_logs_creates_files(tmp_path, monkeypatch):
    monkeypatch.setenv('OPENAI_API_KEY', 'test')
    monkeypatch.chdir(tmp_path)
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    module_path = repo_root / 'trendspire_autoloop.py'
    spec = importlib.util.spec_from_file_location('trendspire_autoloop', module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    mod.ensure_logs()

    assert (tmp_path / mod.LOG_DIR).is_dir()
    assert (tmp_path / mod.MEMORY_DIR).is_dir()
    assert (tmp_path / mod.COST_LOG).is_file()
