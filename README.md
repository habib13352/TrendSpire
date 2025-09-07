<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-09-07 12:24 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [emcie-co/parlant](https://github.com/emcie-co/parlant) | 9372 | Python | LLM agents built for control. Designed for real-world use. Deployed in minutes. |

| [zama-ai/fhevm](https://github.com/zama-ai/fhevm) | 17390 | Rust | FHEVM, a full-stack framework for integrating Fully Homomorphic Encryption (FHE) with blockchain applications |

| [coleam00/ottomator-agents](https://github.com/coleam00/ottomator-agents) | 3965 | Python | All the open source AI Agents hosted on the oTTomator Live Agent Studio platform! |

| [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | 29590 | Rust | An open source payments switch written in Rust to make payments fast, reliable and affordable |

| [FIRST-Tech-Challenge/FtcRobotController](https://github.com/FIRST-Tech-Challenge/FtcRobotController) | 976 | Java | FTC Android Studio Workspace for robot programming in Android Studio |

| [openwrt/openwrt](https://github.com/openwrt/openwrt) | 23571 | C | This repository is a mirror of https://git.openwrt.org/openwrt/openwrt.git It is for reference only and is not active for check-ins. We will continue to accept Pull Requests here. They will be merged via staging trees then into openwrt.git. |

| [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | 8508 | TypeScript | Open Source AI coding assistant for planning, building, and fixing code. We frequently merge features from open-source projects like Roo Code and Cline, while building our own vision. Follow us: kilocode.ai/social |

| [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | 65392 | Java | #1 Locally hosted web application that allows you to perform various operations on PDF files |

| [Eventual-Inc/Daft](https://github.com/Eventual-Inc/Daft) | 3785 | Rust | Distributed query engine providing simple and reliable data processing for any modality and scale |

| [microsoft/BitNet](https://github.com/microsoft/BitNet) | 21637 | Python | Official inference framework for 1-bit LLMs |
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
