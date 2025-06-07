import sys
import pathlib
from unittest import mock

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

import importlib

import trendspire.cli as cli


def test_fetch_subcommand(monkeypatch, capsys):
    monkeypatch.setattr('trendspire.fetch.render_trending', lambda: "md")
    monkeypatch.setattr('trendspire.fetch.update_readme', lambda md: None)
    cli.main(['fetch'])
    out = capsys.readouterr().out
    assert 'Trending digest updated.' in out


def test_ai_patch_subcommand(monkeypatch, tmp_path, capsys):
    readme = tmp_path / 'README.md'
    readme.write_text('hello')
    monkeypatch.setattr('trendspire.ai_patch.load_config', lambda path: {})
    monkeypatch.setattr('trendspire.ai_patch.rewrite_readme', lambda text, cfg: 'new')
    cli.main(['ai-patch', '--readme', str(readme), '--output', str(tmp_path / 'out.md')])
    out = capsys.readouterr().out
    assert 'Wrote improved README' in out
    assert (tmp_path / 'out.md').read_text() == 'new'


def test_ai_readme_subcommand(monkeypatch, capsys):
    monkeypatch.setattr('trendspire.ai_readme.improve_readme', lambda **kw: True)
    cli.main(['ai-readme', '--enable'])
    out = capsys.readouterr().out
    assert 'README updated.' in out
