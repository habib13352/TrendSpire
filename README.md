<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-05-06 01:55 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | 7858 | Rust | Coding agent for DeepSeek models that runs in your terminal |

| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 43757 | TypeScript | 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration |

| [virattt/dexter](https://github.com/virattt/dexter) | 23815 | TypeScript | An autonomous agent for deep financial research |

| [docusealco/docuseal](https://github.com/docusealco/docuseal) | 14042 | Ruby | Open source DocuSign alternative. Create, fill, and sign digital documents ✍️ |

| [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | 7891 | PowerShell | VSCode theme based off the easemate IDE and Jetbrains islands theme |

| [mksglu/context-mode](https://github.com/mksglu/context-mode) | 13077 | TypeScript | Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 14 platforms |

| [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | 8408 | Python | Incremental engine for long horizon agents 🌟 Star if you like it! |

| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 93676 | Shell | A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables. |

| [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | 345839 | Unknown | A complete computer science study plan to become a software engineer. |

| [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | 11350 | Python | A collection of projects showcasing RAG, agents, workflows, and other AI use cases |
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
