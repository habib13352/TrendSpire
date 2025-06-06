import importlib.util
import json
from pathlib import Path


def _load_module(tmp_path, fmt):
    repo_root = Path(__file__).resolve().parents[1]
    module_path = repo_root / 'scripts' / 'summarize_usage.py'
    spec = importlib.util.spec_from_file_location('summarize_usage', module_path)
    mod = importlib.util.module_from_spec(spec)
    import os
    os.environ['API_LOG_FORMAT'] = fmt
    spec.loader.exec_module(mod)
    mod.LOG_DIR = tmp_path
    mod.LOG_FILE = tmp_path / f"api_usage.{fmt}"
    return mod


def _create_log(tmp_path, fmt):
    if fmt == 'csv':
        (tmp_path / 'api_usage.csv').write_text(
            'timestamp,service,model,prompt_tokens,completion_tokens,cost_usd\n'
            't,openai,test,1,2,0.1\n'
        )
    elif fmt == 'json':
        (tmp_path / 'api_usage.json').write_text(
            json.dumps([{
                'timestamp': 't', 'service': 'openai', 'model': 'test',
                'prompt_tokens': 1, 'completion_tokens': 2, 'cost_usd': 0.1
            }])
        )
    else:  # txt
        (tmp_path / 'api_usage.txt').write_text(
            't openai test 1 2 0.1\n'
        )


def _run_and_capture(mod, capsys):
    mod.main()
    return capsys.readouterr().out


def test_summarize_usage_csv(tmp_path, capsys):
    _create_log(tmp_path, 'csv')
    mod = _load_module(tmp_path, 'csv')
    out = _run_and_capture(mod, capsys)
    assert 'test' in out


def test_summarize_usage_json(tmp_path, capsys):
    _create_log(tmp_path, 'json')
    mod = _load_module(tmp_path, 'json')
    out = _run_and_capture(mod, capsys)
    assert 'test' in out


def test_summarize_usage_txt(tmp_path, capsys):
    _create_log(tmp_path, 'txt')
    mod = _load_module(tmp_path, 'txt')
    out = _run_and_capture(mod, capsys)
    assert 'test' in out
