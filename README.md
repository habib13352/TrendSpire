<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-11-08 17:28 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 102707 | Python | Hunt down social media accounts by username across social networks |

| [dsx-ai-factory/nvke](https://github.com/dsx-ai-factory/nvke) | 760 | Go | NVIDIA Kubernetes Engine (NVKE). A management plane for GPU Kubernetes on bare metal. |

| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 17962 | TypeScript | Open-source Grok Bot alternative with a virtual machine that bots can use |

| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | 19285 | Python | A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API |

| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 47410 | Rust | Browser automation CLI for AI agents |

| [meta/astryx](https://github.com/meta/astryx) | 15863 | TypeScript | An open source design system that's fully customizable and agent ready |

| [anthropics/skills](https://github.com/anthropics/skills) | 189352 | Python | Public repository for Agent Skills |

| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 16268 | C++ | Multi-Joint dynamics with Contact. A general purpose physics simulator. |

| [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) | 5002 | TypeScript | A context-compression plugin for month-long single sessions (billions of tokens) ,small context windows (a 100K context is enough) and token savings (5x fewer tokens) .上下文压缩插件，月级长会话会话， 兼顾小窗口(100k上下文足矣)省token(省5倍token) . billion-context is all you need |
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
