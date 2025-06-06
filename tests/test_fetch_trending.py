import importlib.util
import pathlib
from unittest import mock

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(REPO_ROOT))
MODULE_PATH = REPO_ROOT / 'src' / 'fetch_trending.py'
spec = importlib.util.spec_from_file_location('fetch_trending', MODULE_PATH)
ft = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = ft
spec.loader.exec_module(ft)

def test_fetch_trending_fallback_on_error():
    with mock.patch('requests.get', side_effect=Exception('network')):
        results = ft.fetch_trending(limit=1)
    assert results == [ft.FALLBACK_REPO]

