<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-08-16 12:26 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [coleam00/Archon](https://github.com/coleam00/Archon) | 6042 | Python | Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants. |

| [microsoft/poml](https://github.com/microsoft/poml) | 2652 | TypeScript | Prompt Orchestration Markup Language |

| [LMCache/LMCache](https://github.com/LMCache/LMCache) | 4275 | Python | Supercharge Your LLM with the Fastest KV Cache Layer |

| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 410733 | Markdown | Master programming by recreating your favorite technologies from scratch. |

| [farhanashrafdev/90DaysOfCyberSecurity](https://github.com/farhanashrafdev/90DaysOfCyberSecurity) | 10695 | Unknown | This repository contains a 90-day cybersecurity study plan, along with resources and materials for learning various cybersecurity concepts and technologies. The plan is organized into daily tasks, covering topics such as Network+, Security+, Linux, Python, Traffic Analysis, Git, ELK, AWS, Azure, and Hacking. The repository also includes a `LEARN.md |

| [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 86782 | JavaScript |  Now we have become very big, Different from the original idea. Collect premium software in various categories. |

| [tsoding/nob.h](https://github.com/tsoding/nob.h) | 1426 | C | Header only library for writing build recipes in C. |

| [IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge) | 1121 | Python | A Model Context Protocol (MCP) Gateway & Registry. Serves as a central management point for tools, resources, and prompts that can be accessed by MCP-compatible LLM applications. Converts REST API endpoints to MCP, composes virtual MCP servers with added security and observability, and converts between protocols (stdio, SSE, Streamable HTTP). |

| [emcie-co/parlant](https://github.com/emcie-co/parlant) | 3891 | Python | LLM agents built for control. Designed for real-world use. Deployed in minutes. |

| [PixiEditor/PixiEditor](https://github.com/PixiEditor/PixiEditor) | 3335 | C# | PixiEditor is a Universal Editor for all your 2D needs |
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
