<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-07-07 12:29 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 1545 | Rust | 🚀 High-performance distributed object storage for MinIO alternative. |

| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 15035 | Jupyter Notebook | Anthropic's Interactive Prompt Engineering Tutorial |

| [th-ch/youtube-music](https://github.com/th-ch/youtube-music) | 24533 | TypeScript | YouTube Music Desktop App bundled with custom plugins |

| [dockur/macos](https://github.com/dockur/macos) | 14787 | Shell | macOS inside a Docker container. |

| [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase) | 48496 | Go | Open Source realtime backend in 1 file |

| [commaai/openpilot](https://github.com/commaai/openpilot) | 54495 | Python | openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars. |

| [smallcloudai/refact](https://github.com/smallcloudai/refact) | 2442 | Rust | AI Agent that handles engineering tasks end-to-end: integrates with developers’ tools, plans, executes, and iterates until it achieves a successful result. |

| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | 6387 | TypeScript | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? |

| [ed-donner/llm_engineering](https://github.com/ed-donner/llm_engineering) | 2572 | Jupyter Notebook | Repo to accompany my mastering LLM engineering course |

| [CodeWithHarry/Sigma-Web-Dev-Course](https://github.com/CodeWithHarry/Sigma-Web-Dev-Course) | 9103 | JavaScript | Source Code for Sigma Web Development Course |
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
