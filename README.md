<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-08-14 12:30 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [ubicloud/ubicloud](https://github.com/ubicloud/ubicloud) | 8411 | Ruby | Open source alternative to AWS. Elastic compute, block storage (non replicated), firewall and load balancer, managed Postgres, K8s, AI inference, and IAM services. |

| [microsoft/poml](https://github.com/microsoft/poml) | 1868 | TypeScript | Prompt Orchestration Markup Language |

| [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | 31066 | Python | Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG. |

| [external-secrets/external-secrets](https://github.com/external-secrets/external-secrets) | 5357 | Go | External Secrets Operator reads information from a third-party service like AWS Secrets Manager and automatically injects the values as Kubernetes Secrets. |

| [redis/go-redis](https://github.com/redis/go-redis) | 21277 | Go | Redis Go client |

| [colmap/colmap](https://github.com/colmap/colmap) | 9194 | C++ | COLMAP - Structure-from-Motion and Multi-View Stereo |

| [angular/components](https://github.com/angular/components) | 24790 | TypeScript | Component infrastructure and Material Design components for Angular |

| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | 16220 | TypeScript | The Open-sourced Multimodal AI Agent Stack connecting Cutting-edge AI Models and Agent Infra. |

| [midday-ai/midday](https://github.com/midday-ai/midday) | 10438 | TypeScript | Invoicing, Time tracking, File reconciliation, Storage, Financial Overview & your own Assistant made for Freelancers |

| [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | 25405 | Java | Conductor is an event driven orchestration platform providing durable and highly resilient execution engine for your applications |
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
