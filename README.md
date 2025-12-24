<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-12-24 12:31 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [rendercv/rendercv](https://github.com/rendercv/rendercv) | 8128 | Python | Typst-based CV/resume generator for academics and engineers |

| [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | 68370 | Scala | Source code for the X Recommendation Algorithm |

| [google/langextract](https://github.com/google/langextract) | 18908 | Python | A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization. |

| [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | 1516 | Python | A framework for efficient model inference with omni-modality models |

| [stan-smith/FossFLOW](https://github.com/stan-smith/FossFLOW) | 14771 | TypeScript | Make beautiful isometric infrastructure diagrams |

| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | 13519 | Python | CLI tool for configuring and monitoring Claude Code |

| [safety-research/bloom](https://github.com/safety-research/bloom) | 669 | Python | bloom - evaluate any behavior immediately  🌸🌱 |

| [makeplane/plane](https://github.com/makeplane/plane) | 41272 | TypeScript | 🔥 🔥 🔥 Open Source JIRA, Linear, Monday, and Asana Alternative. Plane helps you track your issues, epics, and cycles the easiest way on the planet. |

| [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) | 5669 | Python | RAG on Everything with LEANN. Enjoy 97% storage savings while running a fast, accurate, and 100% private RAG application on your personal device. |

| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | 36392 | Go | Fabric is an open-source framework for augmenting humans using AI. It provides a modular system for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere. |
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
