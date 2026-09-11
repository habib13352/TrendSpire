<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-09-11 02:04 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 38480 | Python | A skill to stop your coding agent from burying the answer. ADHD-friendly output. |

| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 24439 | JavaScript | A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. |

| [obra/superpowers](https://github.com/obra/superpowers) | 284729 | Shell | An agentic skills framework & software development methodology that works. |

| [alsk1992/CloddsBot](https://github.com/alsk1992/CloddsBot) | 1687 | TypeScript | Open Source AI trading agent that operates autonomously across 1000+ markets - Polymarket, Kalshi, Binance, Hyperliquid, Solana DEXs, 5 EVM chains. Scans for edge, executes instantly, manages risk while you sleep. Agent commerce protocol for machine-to-machine payments. Self-hosted. Built on Claude. |

| [Tencent/teamai-cli](https://github.com/Tencent/teamai-cli) | 3831 | TypeScript | Make Every Team AI Native |

| [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | 35766 | Rust | Hundreds of models & providers. One command to find what runs on your hardware. |

| [liquidslr/system-design-notes](https://github.com/liquidslr/system-design-notes) | 18826 | Unknown | Notes of the book System Desgin Interview - An Insider's Guide |

| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 37803 | HTML | 38 editorial diagram types for Claude Code, Codex, and Pi. Self-contained HTML + SVG. No shadows. No Mermaid slop. |

| [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | 30882 | JavaScript | Prompt as Code | GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Skills，新增 2.5 同提示词对比专区，附完整提示词与生成记录，持续更新。 |

| [armory3d/armorpaint](https://github.com/armory3d/armorpaint) | 4433 | C | Graphics Creation Tools |
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
