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

import importlib.util


def test_log_result_tracks_cost(tmp_path, monkeypatch):
    module_path = repo_root / 'ai_loop' / 'logger.py'
    spec = importlib.util.spec_from_file_location('logger', module_path)
    logger = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(logger)
    monkeypatch.setattr(logger, 'LOG_DIR', tmp_path / 'logs')
    monkeypatch.setattr(logger, 'MEMORY_DIR', tmp_path / 'mem')
    monkeypatch.setattr(logger, 'COST_TRACKER', tmp_path / 'mem' / 'cost.csv')
    logger.LOG_DIR.mkdir()
    logger.MEMORY_DIR.mkdir()
    logger.log_result('p', 'r', prompt_tokens=1, completion_tokens=2, cost=0.5)
    rows = logger.COST_TRACKER.read_text().splitlines()
    assert rows[0].startswith('timestamp')
    assert len(rows) == 2
