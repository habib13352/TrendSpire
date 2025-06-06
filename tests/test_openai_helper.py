import importlib
import sys
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

spec = importlib.util.find_spec('src.openai_helper')
openai_helper = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = openai_helper
spec.loader.exec_module(openai_helper)

class DummyResp:
    def __init__(self, content):
        self.choices = [type('Obj', (), {'message': type('Msg', (), {'content': content})})]
        self.usage = type('U', (), {'total_tokens': 10, 'prompt_tokens': 5, 'completion_tokens':5})
        self.choices[0].finish_reason = 'stop'

class DummyClient:
    def __init__(self):
        self.chat = type('Chat', (), {'completions': type('Comp', (), {'create': lambda self, **k: DummyResp('hi')})()})()


def test_get_client_missing_key(monkeypatch):
    monkeypatch.delenv('OPENAI_API_KEY', raising=False)
    with pytest.raises(RuntimeError):
        openai_helper._client = None
        openai_helper._get_client()


def test_ask_openai(monkeypatch):
    monkeypatch.setattr(openai_helper, '_get_client', lambda: DummyClient())
    result = openai_helper.ask_openai('prompt', model='gpt-3.5-turbo')
    assert result == 'hi'

