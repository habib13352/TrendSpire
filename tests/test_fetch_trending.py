from unittest import mock

import trendspire.fetch as ft

def test_fetch_trending_fallback_on_error():
    with mock.patch('requests.get', side_effect=Exception('network')):
        results = ft.fetch_trending(limit=1)
    assert results == [ft.FALLBACK_REPO]

