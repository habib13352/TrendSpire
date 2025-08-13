<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-08-13 12:30 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [ubicloud/ubicloud](https://github.com/ubicloud/ubicloud) | 7439 | Ruby | Open source alternative to AWS. Elastic compute, block storage (non replicated), firewall and load balancer, managed Postgres, K8s, AI inference, and IAM services. |

| [apple/embedding-atlas](https://github.com/apple/embedding-atlas) | 1648 | TypeScript | Embedding Atlas is a tool that provides interactive visualizations for large embeddings. It allows you to visualize, cross-filter, and search embeddings and metadata. |

| [jitsi/jitsi-meet](https://github.com/jitsi/jitsi-meet) | 26246 | TypeScript | Jitsi Meet - Secure, Simple and Scalable Video Conferences that you use as a standalone app or embed in your web application. |

| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | 7886 | Python | Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth! |

| [menloresearch/jan](https://github.com/menloresearch/jan) | 36542 | TypeScript | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer |

| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | 15886 | TypeScript | The Open-sourced Multimodal AI Agent Stack connecting Cutting-edge AI Models and Agent Infra. |

| [FiloSottile/mkcert](https://github.com/FiloSottile/mkcert) | 55594 | Go | A simple zero-config tool to make locally trusted development certificates with any names you'd like. |

| [filamentphp/filament](https://github.com/filamentphp/filament) | 25479 | PHP | A powerful open source UI framework for Laravel • Build and ship admin panels & apps fast with Livewire |

| [open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) | 5588 | Go | OpenTelemetry Collector |

| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 76177 | C++ | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use. |
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
