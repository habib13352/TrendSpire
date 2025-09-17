<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-09-17 12:27 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [category-labs/monad](https://github.com/category-labs/monad) | 305 | C++ | No description provided. |

| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 76708 | Python | Python tool for converting files and office documents to Markdown. |

| [category-labs/monad-bft](https://github.com/category-labs/monad-bft) | 297 | Rust | No description provided. |

| [WebKit/WebKit](https://github.com/WebKit/WebKit) | 9015 | JavaScript | Home of the WebKit project, the browser engine used by Safari, Mail, App Store and many other applications on macOS, iOS and Linux. |

| [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | 25119 | TypeScript | Perplexica is an AI-powered search engine. It is an Open source alternative to Perplexity AI |

| [openai/codex](https://github.com/openai/codex) | 41824 | Rust | Lightweight coding agent that runs in your terminal |

| [nocodb/nocodb](https://github.com/nocodb/nocodb) | 57007 | TypeScript | 🔥 🔥 🔥 Open Source Airtable Alternative |

| [dataease/SQLBot](https://github.com/dataease/SQLBot) | 2084 | Python | 基于大模型和 RAG 的智能问数系统。Text-to-SQL Generation via LLMs using RAG. |

| [google-research/timesfm](https://github.com/google-research/timesfm) | 5567 | Python | TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. |

| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | 40696 | Python | An AI Hedge Fund Team |
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
