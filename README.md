<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-02-20 01:12 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [obra/superpowers](https://github.com/obra/superpowers) | 55395 | Shell | An agentic skills framework & software development methodology that works. |

| [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | 962 | Python | A powerful Telegram bot that provides remote access to Claude Code, enabling developers to interact with their projects from anywhere with full AI assistance and session persistence. |

| [open-mercato/open-mercato](https://github.com/open-mercato/open-mercato) | 722 | TypeScript | AI‑supportive CRM / ERP foundation framework — built to power R&D, new processes, operations, and growth. It’s modular, extensible, and designed for teams that want strong defaults with room to customize everything. Better than Django, Retool and other alternatives - and Enterprise Grade! |

| [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | 20203 | JavaScript | Introduction to Machine Learning Systems |

| [HailToDodongo/pyrite64](https://github.com/HailToDodongo/pyrite64) | 1753 | C++ | N64 Game-Engine and Editor using libdragon & tiny3d |

| [openclaw/openclaw](https://github.com/openclaw/openclaw) | 211903 | TypeScript | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 |

| [freemocap/freemocap](https://github.com/freemocap/freemocap) | 5205 | Python | Free Motion Capture for Everyone 💀✨ |

| [p-e-w/heretic](https://github.com/p-e-w/heretic) | 8494 | Python | Fully automatic censorship removal for language models |
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

## What TrendSpire Does Today

- `python -m src.fetch_trending` — scrape GitHub Trending
- `python -m src.render_digest` — render TRENDING.md & inject into README.md

### AI Agents (coming soon)
See [AGENTS.md](./AGENTS.md) and [ai_loop/README.md](./ai_loop/README.md) for details on the self-improvement loop.

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


## GitHub Actions

### Update Digest

The workflow [`update_digest.yml`](.github/workflows/update_digest.yml) runs every day at 08:00 UTC. It installs the dependencies, executes `python -m src.render_digest`, and commits any changes to `TRENDING.md` and `README.md`.

### Codex Automation

Another workflow [`ai_loop.yml`](.github/workflows/ai_loop.yml) drives the Codex automation using [`ai_loop/autoloop.py`](ai_loop/autoloop.py). It supports two modes:

- **Daily** – diff-based improvements using `gpt-3.5-turbo`.
- **Weekly** – a full repository review with `gpt-4o`.

Each run applies the returned diff, executes the test suite and, when successful, creates a branch and pull request. Summaries, cost logs and the raw diff are saved under `codex_logs/` and uploaded as workflow artifacts. The workflow also caches the `trendspire_memory/` directory so the AI can refine its suggestions over time.

To run the Codex automation locally you can execute:

```bash
python -m ai_loop.autoloop
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
---

### 🗃 Archived & Legacy Code

This repo includes experimental or deprecated files that are not part of the active AI loop. These are stored in:

- `legacy/` – old logic and patch tools
- `archive/` – past metrics and planning reports
- `later/` – utilities planned for future releases (Phase 5+)
