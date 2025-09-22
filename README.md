<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-09-22 12:28 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [Gar-b-age/CookLikeHOC](https://github.com/Gar-b-age/CookLikeHOC) | 12968 | JavaScript | 🥢像老乡鸡🐔那样做饭。主要部分于2024年完工，非老乡鸡官方仓库。文字来自《老乡鸡菜品溯源报告》，并做归纳、编辑与整理。CookLikeHOC. |

| [bevyengine/bevy](https://github.com/bevyengine/bevy) | 42038 | Rust | A refreshingly simple data-driven game engine built in Rust |

| [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | 13515 | Python | Tongyi Deep Research, the Leading Open-source Deep Research Agent |

| [tldraw/tldraw](https://github.com/tldraw/tldraw) | 42381 | TypeScript | very good whiteboard SDK / infinite canvas SDK |

| [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | 73864 | Java | Free and Open Source, Distributed, RESTful Search Engine |

| [torvalds/linux](https://github.com/torvalds/linux) | 202873 | C | Linux kernel source tree |

| [LizardByte/Sunshine](https://github.com/LizardByte/Sunshine) | 29024 | C++ | Self-hosted game stream host for Moonlight. |

| [ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl) | 137592 | Python | Command-line program to download videos from YouTube.com and other video sites |

| [mindcraft-bots/mindcraft](https://github.com/mindcraft-bots/mindcraft) | 3856 | JavaScript | Minecraft AI with LLMs+Mineflayer |

| [eslint/eslint](https://github.com/eslint/eslint) | 26295 | JavaScript | Find and fix problems in your JavaScript code. |
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
