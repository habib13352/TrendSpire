import json
import os
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / 'src' / 'config.json'
ENV_PATH = Path(__file__).resolve().parent.parent / '.env'
EXAMPLE_ENV_PATH = Path(__file__).resolve().parent.parent / '.env.example'

def prompt(prompt_text: str, default: str | None = None) -> str:
    if default:
        user = input(f"{prompt_text} [{default}]: ").strip()
        return user or default
    return input(f"{prompt_text}: ").strip()

def configure_trending() -> None:
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            config = json.load(f)
    else:
        config = {}

    language = prompt('Preferred language (empty for all)', config.get('language', ''))
    since = prompt('Time range (daily/weekly)', config.get('since', 'daily'))
    limit_str = prompt('Number of repositories to fetch', str(config.get('limit', 10)))
    try:
        limit = max(1, int(limit_str))
    except ValueError:
        limit = config.get('limit', 10)

    config.update({'language': language, 'since': since, 'limit': limit})
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    print(f'Saved trending config to {CONFIG_PATH}')

def configure_env() -> None:
    if ENV_PATH.exists():
        current = ENV_PATH.read_text().strip()
    elif EXAMPLE_ENV_PATH.exists():
        current = EXAMPLE_ENV_PATH.read_text().strip()
    else:
        current = 'OPENAI_API_KEY='

    default_key = ''
    for line in current.splitlines():
        if line.startswith('OPENAI_API_KEY='):
            default_key = line.split('=', 1)[1]
            break

    key = prompt('OpenAI API key', default_key)
    lines = []
    for line in current.splitlines():
        if line.startswith('OPENAI_API_KEY='):
            lines.append(f'OPENAI_API_KEY={key}')
        else:
            lines.append(line)
    if 'OPENAI_API_KEY=' not in current:
        lines.append(f'OPENAI_API_KEY={key}')

    ENV_PATH.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'Saved OpenAI key to {ENV_PATH}')

def main() -> None:
    print('--- TrendSpire Setup Wizard ---')
    configure_trending()
    configure_env()
    print('Setup complete! You can now run `python -m src.render_digest`.')

if __name__ == '__main__':
    main()
