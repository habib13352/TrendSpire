from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(REPO_ROOT))

from trendspire import fetch as fetch_trending
from trendspire import ai_readme
from trendspire import utils


def test_fetch_trending_updates(tmp_path, monkeypatch):
    monkeypatch.chdir(REPO_ROOT)
    trending_file = tmp_path / "TRENDING.md"
    trending_file.write_text("initial")

    orig_save = fetch_trending.save_trending
    def _patched(repos, path="TRENDING.md", since="daily"):
        return orig_save(repos, path=trending_file, since=since)
    monkeypatch.setattr(fetch_trending, "save_trending", _patched)

    monkeypatch.setattr(utils, "LOG_DIR", tmp_path / "logs")
    monkeypatch.setattr(utils, "BACKUP_DIR", tmp_path / "backups")

    repos = [fetch_trending.Repo(full_name="test/repo", url="https://github.com/test/repo", description="desc", stars=1, language="Python")]
    with mock.patch.object(fetch_trending, "fetch_trending", return_value=repos):
        fetch_trending.main()

    assert trending_file.exists(), "TRENDING.md not created"
    content = trending_file.read_text()
    assert "test/repo" in content
    backups = list((tmp_path / "backups").glob("TRENDING_*.md"))
    assert backups, "Backup file not created"
    log_text = (tmp_path / "logs" / "update_log.txt").read_text()
    assert "TRENDING updated" in log_text


def test_ai_readme_improves(tmp_path, monkeypatch):
    readme = tmp_path / "README.md"
    readme.write_text("old readme")
    trending = tmp_path / "TRENDING.md"
    trending.write_text("| repo | stars | lang | desc |")

    monkeypatch.setattr(utils, "LOG_DIR", tmp_path / "logs2")
    monkeypatch.setattr(utils, "BACKUP_DIR", tmp_path / "backups2")

    with mock.patch.object(ai_readme, "openai_chat", return_value="new readme"):
        changed = ai_readme.improve_readme(readme, trending, enable=True)

    assert changed
    assert readme.read_text() == "new readme\n"
    backups = list((tmp_path / "backups2").glob("README_*.md"))
    assert backups, "Backup for README not created"
    log_text = (tmp_path / "logs2" / "update_log.txt").read_text()
    assert "README updated" in log_text


def test_is_meaningful_change():
    assert utils.is_meaningful_change("a", "b")
    assert not utils.is_meaningful_change("a", "a")


def test_backup_and_log(tmp_path):
    utils.LOG_DIR = tmp_path / "logs3"
    utils.BACKUP_DIR = tmp_path / "backups3"
    file = tmp_path / "file.txt"
    file.write_text("data")

    backup = utils.backup_file(file)
    assert backup.exists()
    utils.log_update("test", "details")
    log_text = (tmp_path / "logs3" / "update_log.txt").read_text()
    assert "test" in log_text
