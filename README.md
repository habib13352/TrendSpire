<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-07-26 13:05 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat) | 29337 | Swift | bluetooth mesh chat, IRC vibes |

| [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | 4050 | JavaScript | The fastest browser for AI agents to run web automation, built for sharing your logged-in browser state with your AI agents, like Codex or Claude Code, without disturbing you. Zero cost, zero config. |

| [block/buzz](https://github.com/block/buzz) | 12660 | Rust | A hive mind communication platform |

| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 14930 | TypeScript | No description provided. |

| [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | 5379 | TypeScript | The open-source alternative to Webflow, Framer and WordPress. Agentic self-hosted visual CMS outputting clean static pages. Users, roles, plugins, content, database, it's all there. |

| [yorukot/superfile](https://github.com/yorukot/superfile) | 19965 | Go | Pretty fancy and modern terminal file manager |

| [nodejs/node](https://github.com/nodejs/node) | 118403 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |

| [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | 26907 | Java | 🔥🔥🔥 AI-driven database tool and SQL client, The hottest GUI client, supporting MySQL, Oracle, PostgreSQL, DB2, SQL Server, DB2, SQLite, H2, ClickHouse, and more. |

| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 50304 | JavaScript | The design language that makes your AI harness better at design. |

| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | 33981 | Python | Kronos: A Foundation Model for the Language of Financial Markets |
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
