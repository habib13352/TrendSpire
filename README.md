<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-08-19 00:56 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [coleam00/Archon](https://github.com/coleam00/Archon) | 8971 | Python | Beta release of Archon OS - the knowledge and task management backbone for AI coding assistants. |

| [emcie-co/parlant](https://github.com/emcie-co/parlant) | 5654 | Python | LLM agents built for control. Designed for real-world use. Deployed in minutes. |

| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | 36754 | Jupyter Notebook | This is a repo with links to everything you'd ever want to learn about data engineering |

| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 64947 | Jupyter Notebook | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step |

| [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) | 9194 | Unknown | Supercharge your workflow automation with this curated collection of n8n templates! Instantly connect your favorite apps-like Gmail, Telegram, Google Drive, Slack, and more-with ready-to-use, AI-powered automations. Save time, boost productivity, and unlock the true potential of n8n in just a few clicks. |

| [PixiEditor/PixiEditor](https://github.com/PixiEditor/PixiEditor) | 4500 | C# | PixiEditor is a Universal Editor for all your 2D needs |

| [immich-app/immich](https://github.com/immich-app/immich) | 73297 | TypeScript | High performance self-hosted photo and video management solution. |

| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 59579 | Python | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |

| [MotiaDev/motia](https://github.com/MotiaDev/motia) | 6478 | TypeScript | Modern Backend Framework that unifies APIs, background jobs, workflows, and AI agents into a single cohesive system with built-in observability and state management. |

| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | 50228 | Python | Financial data aggregator for humans and AI agents. |
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
