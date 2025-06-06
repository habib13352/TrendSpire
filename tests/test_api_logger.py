import os
import importlib.util
from pathlib import Path
from unittest import mock

MODULE_PATH = Path(__file__).resolve().parents[1] / 'src' / 'api_logger.py'
spec = importlib.util.spec_from_file_location('api_logger', MODULE_PATH)
api_logger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api_logger)


def test_ensure_log_dir_creates_file(tmp_path, monkeypatch):
    log_dir = tmp_path / "logs"
    usage_file = log_dir / "api_usage.csv"
    monkeypatch.setattr(api_logger, "LOG_DIR", log_dir)
    monkeypatch.setattr(api_logger, "USAGE_FILE", usage_file)

    with mock.patch("os.makedirs") as makedirs, \
         mock.patch("os.path.exists", return_value=False), \
         mock.patch("builtins.open", mock.mock_open()) as mopen:
        api_logger.ensure_log_dir()
        makedirs.assert_called_once_with(log_dir, exist_ok=True)
        mopen.assert_called_once_with(usage_file, "w", encoding="utf-8", newline="")


def test_log_openai_usage_writes_entry(tmp_path, monkeypatch):
    log_dir = tmp_path / "logs"
    usage_file = log_dir / "api_usage.csv"
    monkeypatch.setattr(api_logger, "LOG_DIR", log_dir)
    monkeypatch.setattr(api_logger, "USAGE_FILE", usage_file)
    monkeypatch.setattr(api_logger, "ensure_log_dir", lambda: None)

    mopen = mock.mock_open()
    with mock.patch("builtins.open", mopen):
        api_logger.log_openai_usage("model", 10, 20, 0.123456)
        mopen.assert_called_once_with(usage_file, "a", encoding="utf-8", newline="")
        handle = mopen()
        assert handle.write.call_count > 0
