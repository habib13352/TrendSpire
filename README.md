<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-04-18 12:50 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | 1225 | TypeScript | AI You Control: Choose your models. Own your data. Eliminate vendor lock-in. |

| [BasedHardware/omi](https://github.com/BasedHardware/omi) | 10117 | Dart | AI that sees your screen, listens to your conversations and tells you what to do |

| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 22054 | Python | A lightweight, powerful framework for multi-agent workflows |

| [EvoMap/evolver](https://github.com/EvoMap/evolver) | 4749 | JavaScript | The GEP-Powered Self-Evolution Engine for AI Agents. Genome Evolution Protocol. | evomap.ai |

| [deepseek-ai/DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) | 6414 | Cuda | DeepGEMM: clean and efficient FP8 GEMM kernels with fine-grained scaling |

| [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | 31839 | Jupyter Notebook | 《动手学大模型Dive into LLMs》系列编程实践教程 |

| [aaddrick/claude-desktop-debian](https://github.com/aaddrick/claude-desktop-debian) | 3376 | Shell | Claude Desktop for Debian-based Linux distributions |

| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 111836 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |

| [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | 2955 | Shell | Claude Code skill to support Android app's reverse engineering |

| [tractorjuice/arc-kit](https://github.com/tractorjuice/arc-kit) | 595 | HTML | Enterprise Architecture Governance & Vendor Procurement Toolkit |
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
