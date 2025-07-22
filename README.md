<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-07-22 01:00 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [maybe-finance/maybe](https://github.com/maybe-finance/maybe) | 49363 | Ruby | The personal finance app for everyone |

| [ChatGPTNextWeb/NextChat](https://github.com/ChatGPTNextWeb/NextChat) | 84515 | TypeScript | ✨ Light and Fast AI Assistant. Support: Web | iOS | MacOS | Android | Linux | Windows |

| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 5318 | Python | A curated list of awesome commands, files, and workflows for Claude Code |

| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) | 5845 | Python | No description provided. |

| [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) | 28322 | C++ | Hyprland is an independent, highly customizable, dynamic tiling Wayland compositor that doesn't sacrifice on its looks. |

| [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | 312090 | Python | Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. |

| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | 48785 | Python | 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN |

| [Lissy93/dashy](https://github.com/Lissy93/dashy) | 21761 | Vue | 🚀 A self-hostable personal dashboard built for you. Includes status-checking, widgets, themes, icon packs, a UI editor and tons more! |

| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 31515 | Jupyter Notebook | 11 Lessons to Get Started Building AI Agents |

| [better-auth/better-auth](https://github.com/better-auth/better-auth) | 17148 | TypeScript | The most comprehensive authentication framework for TypeScript |
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
