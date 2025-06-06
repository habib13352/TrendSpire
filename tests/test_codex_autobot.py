import os
import time
from pathlib import Path

import importlib.util

os.environ.setdefault("OPENAI_API_KEY", "test")

MODULE_PATH = Path(__file__).resolve().parents[1] / 'ai_loop' / 'codex_autobot.py'
spec = importlib.util.spec_from_file_location('autobot', MODULE_PATH)
autobot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(autobot)


def test_get_target_files_filters(tmp_path):
    (tmp_path / 'a.py').write_text('print("a")')
    (tmp_path / 'b.js').write_text('console.log("b")')
    (tmp_path / 'c.txt').write_text('c')

    files = autobot.get_target_files(tmp_path, exts=['py', 'js'])
    assert len(files) == 2
    assert any(f.endswith('a.py') for f in files)
    assert any(f.endswith('b.js') for f in files)


def test_get_target_files_time_and_size(tmp_path):
    recent = tmp_path / 'recent.py'
    old = tmp_path / 'old.py'
    small = tmp_path / 'small.py'

    recent.write_text('print("hi")')
    old.write_text('print("old")')
    small.write_text('x')

    old_time = time.time() - 86400 * 5  # 5 days ago
    os.utime(old, (old_time, old_time))

    files = autobot.get_target_files(tmp_path, exts=['py'], days=2, min_size=2)
    assert str(recent) in files
    assert str(old) not in files
    assert str(small) not in files
