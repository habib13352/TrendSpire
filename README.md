<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-05-11 02:08 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | 32199 | TypeScript | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra |

| [anthropics/financial-services](https://github.com/anthropics/financial-services) | 18945 | Python | No description provided. |

| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 38516 | Shell | Production-grade engineering skills for AI coding agents. |

| [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | 4816 | Python | Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed. |

| [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | 15620 | Python | "AI-Trader: 100% Fully-Automated Agent-Native Trading" |

| [jundot/omlx](https://github.com/jundot/omlx) | 13329 | Python | LLM inference server with continuous batching & SSD caching for Apple Silicon — managed from the macOS menu bar |

| [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | 9222 | JavaScript | 💻 vibe coding 2026 | Your first modern Coding course for beginners to master step by step. |

| [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | 6851 | TypeScript | 3D Gaussian Splat Editor |

| [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | 10550 | Python | Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption |

| [decolua/9router](https://github.com/decolua/9router) | 7344 | JavaScript | Unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini via 40+ providers. Auto-fallback, RTK -40% tokens, never hit limits. |
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
