<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-08-01 12:31 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [OpenPipe/ART](https://github.com/OpenPipe/ART) | 4392 | Python | Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen2.5, Qwen3, Llama, Kimi, and more! |

| [TandoorRecipes/recipes](https://github.com/TandoorRecipes/recipes) | 6565 | HTML | Application for managing recipes, planning meals, building shopping lists and much much more! |

| [devlikeapro/waha](https://github.com/devlikeapro/waha) | 2421 | TypeScript | WAHA - WhatsApp HTTP API (REST API) that you can configure in a click! 3 engines: WEBJS (browser based), NOWEB (websocket nodejs), GOWS (websocket go) |

| [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | 91476 | TypeScript | JavaScript API for Chrome and Firefox |

| [kubesphere/kubesphere](https://github.com/kubesphere/kubesphere) | 16222 | Go | The container platform tailored for Kubernetes multi-cloud, datacenter, and edge management ⎈ 🖥 ☁️ |

| [eclipse-sumo/sumo](https://github.com/eclipse-sumo/sumo) | 2978 | C++ | Eclipse SUMO is an open source, highly portable, microscopic and continuous traffic simulation package designed to handle large networks. It allows for intermodal simulation including pedestrians and comes with a large set of tools for scenario creation. |

| [9001/copyparty](https://github.com/9001/copyparty) | 17151 | Python | Portable file server with accelerated resumable uploads, dedup, WebDAV, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no deps |

| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | 2747 | TypeScript | Free, local, open-source AI app builder | v0 / lovable / Bolt alternative | 🌟 Star if you like it! |

| [stenzek/duckstation](https://github.com/stenzek/duckstation) | 8767 | C++ | Fast PlayStation 1 emulator for x86-64/AArch32/AArch64/RV64 |

| [playcanvas/editor](https://github.com/playcanvas/editor) | 362 | TypeScript | Powerful visual editor environment for building WebGL, WebGPU, WebXR apps |
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
