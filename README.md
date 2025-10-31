<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-31 12:29 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | 88716 | Shell | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |

| [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | 4600 | JavaScript | CRS-自建Claude Code镜像，一站式开源中转服务，让 Claude、OpenAI、Gemini、Droid 订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。 |

| [ventoy/Ventoy](https://github.com/ventoy/Ventoy) | 71753 | C | A new bootable USB solution. |

| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates) | 11185 | JavaScript | Community curated list of templates for the nuclei engine to find security vulnerabilities. |

| [fmtlib/fmt](https://github.com/fmtlib/fmt) | 22770 | C++ | A modern formatting library |

| [qeeqbox/social-analyzer](https://github.com/qeeqbox/social-analyzer) | 16611 | JavaScript | API, CLI, and Web App for analyzing and finding a person's profile in 1000 social media \ websites |

| [open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) | 6110 | Go | OpenTelemetry Collector |

| [yhirose/cpp-httplib](https://github.com/yhirose/cpp-httplib) | 15338 | C++ | A C++ header-only HTTP/HTTPS server and client library |

| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | 4577 | Python | The absolute trainer to light up AI agents. |

| [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | 2144 | Python | 微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。 |
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
