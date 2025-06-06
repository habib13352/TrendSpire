<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-06-06 08:59 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [frdel/agent-zero](https://github.com/frdel/agent-zero) | 8957 | Python | Agent Zero AI framework |

| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | 8037 | Python | A high-performance algorithmic trading platform and event-driven backtester |

| [scrapy/scrapy](https://github.com/scrapy/scrapy) | 56263 | Python | Scrapy, a fast high-level web crawling & scraping framework for Python. |

| [onlook-dev/onlook](https://github.com/onlook-dev/onlook) | 16787 | TypeScript | The Cursor for Designers • An Open-Source Visual Vibecoding Editor • Visually build, style, and edit your React App with AI |

| [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) | 88114 | Dockerfile | 程序员在家做饭方法指南。Programmer's guide about how to cook at home (Simplified Chinese only). |

| [netbirdio/netbird](https://github.com/netbirdio/netbird) | 14199 | Go | Connect your devices into a secure WireGuard®-based overlay network with SSO, MFA and granular access controls. |

| [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | 4683 | Kotlin | 🪐 Markdown with superpowers — from ideas to presentations, articles and books. |

| [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 36601 | Roff | 所有小初高、大学PDF教材。 |

| [ArduPilot/ardupilot](https://github.com/ArduPilot/ardupilot) | 12645 | C++ | ArduPlane, ArduCopter, ArduRover, ArduSub source |

| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 3064 | Python | Memory for AI Agents in 5 lines of code |
<!-- TRENDING_END -->

# TrendSpire

TrendSpire gathers trending repositories from GitHub and stores them in `TRENDING.md`. GitHub Actions keep the digest fresh and leverage OpenAI Codex to continuously improve the codebase.

## Features

- Automated scraping of GitHub's trending page with configurable language, time range and result limit.
- Daily workflow to regenerate `TRENDING.md` and update this README.
- Scheduled Codex runs that suggest small refactors and new tests via pull requests.
- Token and cost tracking for all Codex requests.
- Persistent memory stored under `trendspire_memory/` enables the AI to
  iteratively refine its suggestions across runs and open automated pull
  requests with context.

## Getting Started

1. **Install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the setup wizard**
   ```bash
   python scripts/setup_wizard.py
   ```
   This interactive script stores your preferred trending options and OpenAI API key.
   You can rerun it at any time to change the configuration.

3. **Run the trending scraper**
   ```bash
   python -m src.render_digest
   ```
   The latest results will appear in `TRENDING.md` and the README.

4. **Run the self-improvement loop**
   With your virtual environment active run:
   ```bash
   python trendspire_autoloop.py --mode daily
   ```
   Replace `daily` with `weekly` for a full project review. The script stores its
   diff history under `trendspire_memory/`, applies the changes, runs the tests
   and opens a pull request when successful.

5. **Enable the PR workflow**
   Ensure GitHub Actions are enabled on your fork. The workflow will reuse the
   cached memory directory and automatically open pull requests on a schedule.

## GitHub Actions

### Update Digest

The workflow [`update_digest.yml`](.github/workflows/update_digest.yml) runs every day at 08:00 UTC. It installs the dependencies, executes `python -m src.render_digest`, and commits any changes to `TRENDING.md` and `README.md`.

### Codex Automation

Another workflow [`auto_codex_mixed.yml`](.github/workflows/auto_codex_mixed.yml) drives the Codex automation using [`trendspire_autoloop.py`](trendspire_autoloop.py). It supports two modes:

- **Daily** – diff-based improvements using `gpt-3.5-turbo`.
- **Weekly** – a full repository review with `gpt-4o`.

Each run applies the returned diff, executes the test suite and, when successful, creates a branch and pull request. Summaries, cost logs and the raw diff are saved under `codex_logs/` and uploaded as workflow artifacts. The workflow also caches the `trendspire_memory/` directory so the AI can refine its suggestions over time.

To run the Codex automation locally you can execute:

```bash
python trendspire_autoloop.py --mode daily   # or weekly
```

### API usage reports

The file `logs/api_usage.*` records token counts and cost. Set `API_LOG_FORMAT`
to `csv`, `json` or `txt` to control the format. Run `python
scripts/summarize_usage.py` for a quick summary grouped by model.

### Running tests

After installing the requirements you can run the entire test suite with

```bash
pytest
```

Additional tips for contributors are available in
[docs/DEVELOPER.md](docs/DEVELOPER.md).
