import importlib.util
import pathlib
from unittest import mock

MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / 'src' / 'fetch_trending.py'
spec = importlib.util.spec_from_file_location('fetch_trending', MODULE_PATH)
ft = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ft)

def test_fetch_trending_fallback_on_error():
    with mock.patch('requests.get', side_effect=Exception('network')):
        results = ft.fetch_trending(limit=1)
    assert results == [ft.FALLBACK_REPO]

