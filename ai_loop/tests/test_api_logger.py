import importlib.util
import json
from pathlib import Path


def _load_module(tmp_path, fmt):
    repo_root = Path(__file__).resolve().parents[2]
    module_path = repo_root / 'ai_loop' / 'api_logger.py'
    spec = importlib.util.spec_from_file_location('api_logger', module_path)
    api_logger = importlib.util.module_from_spec(spec)
    # Set environment variable before loading
    import os
    os.environ['API_LOG_FORMAT'] = fmt
    spec.loader.exec_module(api_logger)
    api_logger.LOG_DIR = tmp_path
    api_logger.USAGE_FILE = tmp_path / f"api_usage.{api_logger.LOG_FORMAT}"
    return api_logger


def test_log_openai_usage_json(tmp_path):
    api_logger = _load_module(tmp_path, 'json')
    api_logger.log_openai_usage('test-model', 1, 2, 0.001)
    data = json.loads((tmp_path / 'api_usage.json').read_text())
    assert data and data[0]['model'] == 'test-model'


def test_log_openai_usage_txt(tmp_path):
    api_logger = _load_module(tmp_path, 'txt')
    api_logger.log_openai_usage('test-model', 3, 4, 0.123456)
    content = (tmp_path / 'api_usage.txt').read_text()
    assert 'test-model' in content
