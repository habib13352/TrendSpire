<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-06-29 01:04 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [twentyhq/twenty](https://github.com/twentyhq/twenty) | 30424 | TypeScript | Building a modern alternative to Salesforce, powered by the community. |

| [black-forest-labs/flux](https://github.com/black-forest-labs/flux) | 22908 | Python | Official inference repo for FLUX.1 models |

| [GraphiteEditor/Graphite](https://github.com/GraphiteEditor/Graphite) | 13790 | Rust | 2D vector & raster editor that melds traditional layers & tools with a modern node-based, non-destructive, procedural workflow. |

| [adityachandelgit/BookLore](https://github.com/adityachandelgit/BookLore) | 1835 | Java | BookLore is a web app for hosting, managing, and exploring books, with support for PDFs, eBooks, reading progress, metadata, and stats. |

| [coleam00/ottomator-agents](https://github.com/coleam00/ottomator-agents) | 2919 | Python | All the open source AI Agents hosted on the oTTomator Live Agent Studio platform! |

| [rommapp/romm](https://github.com/rommapp/romm) | 5001 | Python | A beautiful, powerful, self-hosted rom manager and player. |

| [Serial-Studio/Serial-Studio](https://github.com/Serial-Studio/Serial-Studio) | 5758 | C++ | Visualize embedded device data. |

| [midday-ai/midday](https://github.com/midday-ai/midday) | 8189 | TypeScript | Invoicing, Time tracking, File reconciliation, Storage, Financial Overview & your own Assistant made for Freelancers |

| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 86379 | Jupyter Notebook | 21 Lessons, Get Started Building with Generative AI 🔗 https://microsoft.github.io/generative-ai-for-beginners/ |

| [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | 33948 | TypeScript | Full stack, modern web application template. Using FastAPI, React, SQLModel, PostgreSQL, Docker, GitHub Actions, automatic HTTPS and more. |
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
