<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-07-12 12:26 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [snap-stanford/Biomni](https://github.com/snap-stanford/Biomni) | 1393 | Python | Biomni: a general-purpose biomedical AI agent |

| [open-telemetry/opentelemetry-go](https://github.com/open-telemetry/opentelemetry-go) | 5877 | Go | OpenTelemetry Go API and SDK |

| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | 5766 | Go | MCP Toolbox for Databases is an open source MCP server for databases. |

| [protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf) | 68442 | C++ | Protocol Buffers - Google's data interchange format |

| [getzep/graphiti](https://github.com/getzep/graphiti) | 12590 | Python | Build Real-Time Knowledge Graphs for AI Agents |

| [pybind/pybind11](https://github.com/pybind/pybind11) | 16925 | C++ | Seamless operability between C++11 and Python |

| [WordPress/wordpress-develop](https://github.com/WordPress/wordpress-develop) | 2974 | PHP | WordPress Develop, Git-ified. Synced from git://develop.git.wordpress.org/, including branches and tags! This repository is just a mirror of the WordPress subversion repository. Please include a link to a pre-existing ticket on https://core.trac.wordpress.org/ with every pull request. |

| [gorhill/uBlock](https://github.com/gorhill/uBlock) | 55270 | JavaScript | uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean. |

| [landing-ai/agentic-doc](https://github.com/landing-ai/agentic-doc) | 882 | Python | Python library for Agentic Document Extraction from LandingAI |

| [zijie0/HumanSystemOptimization](https://github.com/zijie0/HumanSystemOptimization) | 19339 | Unknown | 健康学习到150岁 - 人体系统调优不完全指南 |
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
