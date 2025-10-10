<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-10 00:52 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | 6718 | JavaScript | Stremio - Freedom to Stream |

| [MODSetter/SurfSense](https://github.com/MODSetter/SurfSense) | 8878 | Python | Open Source Alternative to NotebookLM / Perplexity, connected to external sources such as Search Engines, Slack, Linear, Jira, ClickUp, Confluence, Notion, YouTube, GitHub, Discord and more. Join our discord: https://discord.gg/ejRNvftDp9 |

| [google/computer-use-preview](https://github.com/google/computer-use-preview) | 653 | Python | No description provided. |

| [TibixDev/winboat](https://github.com/TibixDev/winboat) | 8280 | TypeScript | Run Windows apps on 🐧 Linux with ✨ seamless integration |

| [timelinize/timelinize](https://github.com/timelinize/timelinize) | 2170 | Go | Store your data from all your accounts and devices in a single cohesive timeline on your own computer |

| [rust-lang/rustfmt](https://github.com/rust-lang/rustfmt) | 6539 | Rust | Format Rust code |

| [PixelGuys/Cubyz](https://github.com/PixelGuys/Cubyz) | 1127 | Zig | Voxel sandbox game with a large render distance, procedurally generated content and some cool graphical effects. |

| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 15973 | Python | A lightweight, powerful framework for multi-agent workflows |

| [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 52121 | Roff | 所有小初高、大学PDF教材。 |

| [browserbase/stagehand](https://github.com/browserbase/stagehand) | 17877 | TypeScript | The AI Browser Automation Framework |
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
