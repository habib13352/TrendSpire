<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-01 00:58 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 43698 | Python | 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. |

| [nextcloud/server](https://github.com/nextcloud/server) | 31302 | PHP | ☁️ Nextcloud server, a safe home for all your data |

| [typst/typst](https://github.com/typst/typst) | 46363 | Rust | A new markup-based typesetting system that is powerful and easy to learn. |

| [fastapi/fastapi](https://github.com/fastapi/fastapi) | 90158 | Python | FastAPI framework, high performance, easy to learn, fast to code, ready for production |

| [commaai/openpilot](https://github.com/commaai/openpilot) | 57920 | Python | openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars. |

| [DevCaress/guia-entrevistas-de-programacion](https://github.com/DevCaress/guia-entrevistas-de-programacion) | 6050 | Unknown | No description provided. |

| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | 1502 | Python | No description provided. |

| [juliangarnier/anime](https://github.com/juliangarnier/anime) | 64340 | JavaScript | JavaScript animation engine |

| [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | 339054 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |

| [Done-0/fuck-u-code](https://github.com/Done-0/fuck-u-code) | 4517 | Go | Legacy-Mess Detector – assess the “legacy-mess level” of your code and output a beautiful report | 屎山代码检测器，评估代码的“屎山等级”并输出美观的报告 |
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
