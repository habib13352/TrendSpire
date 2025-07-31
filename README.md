<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-07-31 12:30 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) | 3553 | Python | No description provided. |

| [stenzek/duckstation](https://github.com/stenzek/duckstation) | 8565 | C++ | Fast PlayStation 1 emulator for x86-64/AArch32/AArch64/RV64 |

| [SkyworkAI/SkyReels-V2](https://github.com/SkyworkAI/SkyReels-V2) | 3728 | Python | SkyReels-V2: Infinite-length Film Generative model |

| [OpenPipe/ART](https://github.com/OpenPipe/ART) | 4001 | Python | Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen2.5, Qwen3, Llama, Kimi, and more! |

| [EmenstaNougat/ESP32-BlueJammer](https://github.com/EmenstaNougat/ESP32-BlueJammer) | 3382 | Unknown | The ESP32-BlueJammer (Bluetooth jammer, BLE jammer, WiFi jammer, RC jammer) disrupts 2.4GHz communications. Using an ESP32 and nRF24 modules, it generates noise and unnecessary packets, causing interference between the devices communicating, making them unable to work as intended. Ideal for controlled disruption and security testing. |

| [9001/copyparty](https://github.com/9001/copyparty) | 15510 | Python | Portable file server with accelerated resumable uploads, dedup, WebDAV, FTP, TFTP, zeroconf, media indexer, thumbnails++ all in one file, no deps |

| [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | 91323 | TypeScript | JavaScript API for Chrome and Firefox |

| [Canner/WrenAI](https://github.com/Canner/WrenAI) | 9001 | TypeScript | ⚡️Wren AI is your GenBI Agent, that you can query any database with natural language, get accurate SQL(Text-to-SQL), charts(Text-to-Charts) & AI-generated insights in seconds. |

| [pointfreeco/swift-composable-architecture](https://github.com/pointfreeco/swift-composable-architecture) | 13533 | Swift | A library for building applications in a consistent and understandable way, with composition, testing, and ergonomics in mind. |

| [fastrepl/hyprnote](https://github.com/fastrepl/hyprnote) | 3460 | TypeScript | Local-first AI Notepad for Private Meetings |
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
