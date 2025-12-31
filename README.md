<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-12-31 12:30 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [afkarxyz/SpotiFLAC](https://github.com/afkarxyz/SpotiFLAC) | 1301 | TypeScript | Get Spotify tracks in true FLAC from Tidal, Qobuz & Amazon Music — no account required. |

| [google-gemini/computer-use-preview](https://github.com/google-gemini/computer-use-preview) | 2231 | Python | No description provided. |

| [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | 13561 | JavaScript | Introduction to Machine Learning Systems |

| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | 9872 | Rust | Get 10X more out of Claude Code, Codex or any coding agent |

| [timescale/pg-aiguide](https://github.com/timescale/pg-aiguide) | 933 | Python | MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code. |

| [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | 41695 | Python | 🎯 告别信息过载，AI 助你看懂新闻资讯热点，支持 RSS 订阅，简单的舆情监控分析 - 多平台热点聚合+基于 MCP 的AI分析工具。监控35个平台（抖音、知乎、B站、华尔街见闻、财联社等），智能筛选+自动推送+AI对话分析（用自然语言深度挖掘新闻：趋势追踪、情感分析、相似检索等20种工具）。支持企业微信/个人微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 推送，30秒快速部署，1分钟手机通知，无需编程。支持Docker部署，支持数据远程云存储⭐ 让算法为你服务，用AI理解热点 |

| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 70108 | Jupyter Notebook | Examples and guides for using the OpenAI API |

| [organicmaps/organicmaps](https://github.com/organicmaps/organicmaps) | 12442 | C++ | 🍃 Organic Maps is a free Android & iOS offline maps app for travelers, tourists, hikers, and cyclists. It uses crowd-sourced OpenStreetMap data and is developed with love by the community. No ads, no tracking, no data collection, no crapware. Please donate to support the development! |

| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | 19849 | Python | SoTA open-source TTS |

| [nocodb/nocodb](https://github.com/nocodb/nocodb) | 59483 | TypeScript | 🔥 🔥 🔥 Open Source Airtable Alternative |
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
