"""Check that automation ran successfully and report problems."""
from __future__ import annotations

import os
from datetime import datetime, timedelta
from pathlib import Path
import requests

LOG_FILE = Path('logs/update_log.txt')
ACTIONS_URL = os.environ.get('GITHUB_SERVER_URL', 'https://github.com') + '/' + os.environ.get('GITHUB_REPOSITORY', '') + '/actions'

def _last_timestamp(action: str) -> datetime | None:
    if not LOG_FILE.exists():
        return None
    for line in reversed(LOG_FILE.read_text().splitlines()):
        if f'] {action}:' in line:
            ts = line.split(']')[0].strip('[')
            try:
                return datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return None
    return None

def notify(message: str) -> None:
    token = os.environ.get('GITHUB_TOKEN')
    repo = os.environ.get('GITHUB_REPOSITORY')
    if token and repo:
        url = f'https://api.github.com/repos/{repo}/issues'
        requests.post(url, headers={'Authorization': f'token {token}'}, json={'title': 'Automation monitor alert', 'body': message})


def main() -> None:
    trending = _last_timestamp('TRENDING updated')
    readme = _last_timestamp('README updated')
    now = datetime.utcnow()
    ok = True
    if not trending or now - trending > timedelta(hours=24):
        ok = False
    if not readme or now - readme > timedelta(hours=24):
        ok = False
    if ok:
        print('Automation healthy')
    else:
        msg = f'Automation failed or delayed. See logs: {ACTIONS_URL}'
        notify(msg)
        print(msg)

if __name__ == '__main__':
    main()
