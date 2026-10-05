<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-10-05 03:02 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [tester-army/e2e](https://github.com/tester-army/e2e) | 3240 | TypeScript | Next generation e2e testing framework for web and mobile apps. |

| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 76375 | JavaScript | The design language that makes your AI harness better at design. |

| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 53128 | JavaScript | Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering. |

| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 154985 | JavaScript | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. |

| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | 16908 | Python | Give your agent CAD superpowers. |

| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 90992 | Python | Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees. |

| [getsentry/sentry](https://github.com/getsentry/sentry) | 45404 | Python | Developer-first error tracking and performance monitoring |

| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 63274 | Python | World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio. |

| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 25212 | TypeScript | No description provided. |

| [caddyserver/caddy](https://github.com/caddyserver/caddy) | 76605 | Go | Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS |
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
