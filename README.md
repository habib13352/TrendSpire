<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-06-06 07:31 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [frdel/agent-zero](https://github.com/frdel/agent-zero) | 8934 | Python | Agent Zero AI framework |

| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | 8005 | Python | A high-performance algorithmic trading platform and event-driven backtester |

| [scrapy/scrapy](https://github.com/scrapy/scrapy) | 56232 | Python | Scrapy, a fast high-level web crawling & scraping framework for Python. |

| [onlook-dev/onlook](https://github.com/onlook-dev/onlook) | 16756 | TypeScript | The Cursor for Designers • An Open-Source Visual Vibecoding Editor • Visually build, style, and edit your React App with AI |

| [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) | 88068 | Dockerfile | 程序员在家做饭方法指南。Programmer's guide about how to cook at home (Simplified Chinese only). |

| [netbirdio/netbird](https://github.com/netbirdio/netbird) | 14190 | Go | Connect your devices into a secure WireGuard®-based overlay network with SSO, MFA and granular access controls. |

| [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | 4623 | Kotlin | 🪐 Markdown with superpowers — from ideas to presentations, articles and books. |

| [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 36540 | Roff | 所有小初高、大学PDF教材。 |

| [ArduPilot/ardupilot](https://github.com/ArduPilot/ardupilot) | 12627 | C++ | ArduPlane, ArduCopter, ArduRover, ArduSub source |

| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 3037 | Python | Memory for AI Agents in 5 lines of code |
<!-- TRENDING_END -->

# TrendSpire

TrendSpire scrapes GitHub's trending page and generates a markdown digest of popular repositories. A GitHub Action keeps the `TRENDING.md` file updated on a daily schedule.

## Getting Started

1. **Install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run locally**
   ```bash
   python -m src.render_digest
   ```
   The latest trending list will be written to `TRENDING.md`.

3. **Configuration**
   Edit `src/config.json` to set your preferred language, time range (`daily` or `weekly`), and number of repositories to include.
   An example configuration looks like:
   ```json
   {
     "language": "",
     "since": "daily",
     "limit": 10
   }
    ```
    After updating the configuration, run `python -m src.render_digest` again to regenerate `TRENDING.md`.

4. **Set up OpenAI API key**
   Copy `.env.example` to `.env` and replace the placeholder value with your
   actual `OPENAI_API_KEY`. The automation script will load this file
   automatically when contacting the OpenAI API.

## GitHub Action

The workflow in `.github/workflows/update_digest.yml` regenerates the digest every day at 08:00 UTC and commits changes automatically.

## Codex Automation

This repository uses an additional GitHub Actions workflow (`auto_codex_mixed.yml`) to
run OpenAI Codex on a schedule. The orchestrator script `trendspire_codex_mixed.py`
manages daily and weekly runs:

* **Daily** (`--mode daily`)
  - Fetches the diff for files under `src/` relative to `origin/main`.
  - Sends that diff to `gpt-3.5-turbo` asking for small refactors, logging and test
    additions.
  - Applies the returned unified diff and runs `pytest`.
  - If tests pass, a branch `codex-daily-<timestamp>` is pushed and a pull request is
    opened automatically.

* **Weekly** (`--mode weekly`)
  - Concatenates all Python files in `src/` and sends them to `code-davinci-002` for a
    deeper refactor and additional tests.
  - Applies the diff, runs the test suite and creates a `codex-weekly-<timestamp>` pull
    request when successful.

Token usage and cost for each run are appended to `codex_costs.csv`. Detailed logs are
stored in the `codex_logs/` directory and uploaded as workflow artifacts. The daily job
runs at 02:00 UTC and the weekly job every Sunday at 03:00 UTC.

### API usage logs

OpenAI API usage from the Codex runs is also written to `logs/api_usage.csv`. Each entry records the timestamp, model, token counts and cost in USD. To see a quick summary grouped by model run:

```bash
python scripts/summarize_usage.py
```

