<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-08-27 00:53 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 11637 | JavaScript | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |

| [plait-board/drawnix](https://github.com/plait-board/drawnix) | 8980 | TypeScript | 开源白板工具（SaaS），一体化白板，包含思维导图、流程图、自由画等。All in one open-source whiteboard tool with mind, flowchart, freehand and etc. |

| [willccbb/verifiers](https://github.com/willccbb/verifiers) | 2462 | Python | Verifiers for LLM Reinforcement Learning |

| [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) | 4079 | Python | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |

| [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java) | 63024 | Java | All Algorithms implemented in Java |

| [MODSetter/SurfSense](https://github.com/MODSetter/SurfSense) | 6834 | Python | Open Source Alternative to NotebookLM / Perplexity, connected to external sources such as Search Engines, Slack, Linear, Jira, ClickUp, Confluence, Notion, YouTube, GitHub, Discord and more. Join our discord: https://discord.gg/ejRNvftDp9 |

| [eythaann/Seelen-UI](https://github.com/eythaann/Seelen-UI) | 10958 | Rust | The Fully Customizable Desktop Environment for Windows 10/11. |

| [SimplifyJobs/Summer2026-Internships](https://github.com/SimplifyJobs/Summer2026-Internships) | 40396 | Unknown | Collection of Summer 2026 tech internships! |

| [tw93/Pake](https://github.com/tw93/Pake) | 41461 | JavaScript | 🤱🏻 Turn any webpage into a desktop app with Rust. 🤱🏻 利用 Rust 轻松构建轻量级多端桌面应用 |

| [GitHubDaily/GitHubDaily](https://github.com/GitHubDaily/GitHubDaily) | 41193 | Unknown | 坚持分享 GitHub 上高质量、有趣实用的开源技术教程、开发者工具、编程网站、技术资讯。A list cool, interesting projects of GitHub. |
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
