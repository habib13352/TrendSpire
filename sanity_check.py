"""Simple sanity checks before merging automation results."""
from __future__ import annotations

from pathlib import Path
from utils import is_meaningful_change


def main() -> None:
    ok = True
    trending = Path('TRENDING.md')
    if not trending.exists():
        print('TRENDING.md missing')
        ok = False
    readme = Path('README.md')
    if not readme.exists():
        print('README.md missing')
        ok = False
    log_file = Path('logs/update_log.txt')
    if not log_file.exists():
        print('log file missing')
        ok = False
    if ok:
        print('Sanity check passed')
    else:
        raise SystemExit('Sanity check failed')

if __name__ == '__main__':
    main()
