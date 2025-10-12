<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-12 12:24 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 37386 | TypeScript | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |

| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | 7343 | JavaScript | CLI tool for configuring and monitoring Claude Code |

| [evershopcommerce/evershop](https://github.com/evershopcommerce/evershop) | 6923 | TypeScript | 🛍️ Typescript E-commerce Platform |

| [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | 19759 | C++ | An MCP-based chatbot | 一个基于MCP的聊天机器人 |

| [daytonaio/daytona](https://github.com/daytonaio/daytona) | 22572 | TypeScript | Daytona is a Secure and Elastic Infrastructure for Running AI-Generated Code |

| [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 52987 | Roff | 所有小初高、大学PDF教材。 |

| [WECENG/ticket-purchase](https://github.com/WECENG/ticket-purchase) | 4754 | Python | 大麦自动抢票，支持人员、城市、日期场次、价格选择 |

| [DIYgod/RSSHub](https://github.com/DIYgod/RSSHub) | 39073 | TypeScript | 🧡 Everything is RSSible |

| [DearVa/Everywhere](https://github.com/DearVa/Everywhere) | 358 | C# | A context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools. |

| [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) | 94783 | Dockerfile | 程序员在家做饭方法指南。Programmer's guide about how to cook at home (Simplified Chinese only). |
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
