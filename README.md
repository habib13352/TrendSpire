<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-04-25 01:26 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | 9008 | Python | Use claude-code for free in the terminal, VSCode extension or via discord like openclaw |

| [huggingface/ml-intern](https://github.com/huggingface/ml-intern) | 5362 | Python | 🤗 ml-intern: an open-source ML engineer that reads papers, trains models, and ships ML models |

| [google/osv-scanner](https://github.com/google/osv-scanner) | 9515 | Go | Vulnerability scanner written in Go which uses the data provided by https://osv.dev |

| [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | 62390 | Python | ALL IN ONE Hacking Tool For Hackers |

| [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | 9017 | TypeScript | Code search MCP for Claude Code. Make entire codebase the context for any coding agent. |

| [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | 13357 | TypeScript | OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration. |

| [PostHog/posthog](https://github.com/PostHog/posthog) | 33118 | Python | 🦔 PostHog is an all-in-one developer platform for building successful products. We offer product analytics, web analytics, session replay, error tracking, feature flags, experimentation, surveys, data warehouse, a CDP, and an AI product assistant to help debug your code, ship features faster, and keep all your usage and customer data in one stack. |

| [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden) | 59176 | Rust | Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs |

| [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | 7699 | JavaScript | Uncensored, open-source alternative to Higgsfield AI, Freepik AI, Krea AI, Openart AI — Free, unrestricted AI image & video generation studio with 200+ models (Flux, Midjourney, Kling, Sora, Veo). No content filters. Self-hosted, MIT licensed. |

| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 494799 | Markdown | Master programming by recreating your favorite technologies from scratch. |
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
