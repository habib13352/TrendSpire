<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-12-08 12:31 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | 13229 | Python | Open-Source Frontier Voice AI |

| [sinelaw/fresh](https://github.com/sinelaw/fresh) | 1172 | Rust | Text editor for your terminal: easy, powerful and fast |

| [winapps-org/winapps](https://github.com/winapps-org/winapps) | 13122 | Shell | Run Windows apps such as Microsoft Office/Adobe in Linux (Ubuntu/Fedora) and GNOME/KDE as if they were a part of the native OS, including Nautilus integration. Hard fork of https://github.com/Fmstrat/winapps/ |

| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | 22134 | Jupyter Notebook | In-depth tutorials on LLMs, RAGs and real-world AI agent applications. |

| [slidevjs/slidev](https://github.com/slidevjs/slidev) | 42463 | TypeScript | Presentation Slides for Developers |

| [cloudflare/vibesdk](https://github.com/cloudflare/vibesdk) | 3524 | TypeScript | An open-source vibe coding platform that helps you build your own vibe-coding platform, built entirely on Cloudflare stack |

| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 12948 | TypeScript | An Open Source implementation of Notebook LM with more flexibility and features |

| [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | 11313 | Python | A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API |

| [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | 31454 | Python | 微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。 |

| [microsoft/Foundry-Local](https://github.com/microsoft/Foundry-Local) | 1490 | Svelte | No description provided. |
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
