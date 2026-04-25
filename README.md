<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-04-25 12:51 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | 10644 | Python | Use claude-code for free in the terminal, VSCode extension or via discord like openclaw |

| [mattpocock/skills](https://github.com/mattpocock/skills) | 18870 | Shell | My personal directory of skills, straight from my .claude directory. |

| [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | 62973 | Python | ALL IN ONE Hacking Tool For Hackers |

| [PostHog/posthog](https://github.com/PostHog/posthog) | 33326 | Python | 🦔 PostHog is an all-in-one developer platform for building successful products. We offer product analytics, web analytics, session replay, error tracking, feature flags, experimentation, surveys, data warehouse, a CDP, and an AI product assistant to help debug your code, ship features faster, and keep all your usage and customer data in one stack. |

| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | 25184 | Python | CLI tool for configuring and monitoring Claude Code |

| [deepseek-ai/DeepEP](https://github.com/deepseek-ai/DeepEP) | 9418 | Cuda | DeepEP: an efficient expert-parallel communication library |

| [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | 52940 | C# | PowerShell for every system! |

| [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) | 23397 | TypeScript | Roo Code gives you a whole dev team of AI agents in your code editor. |

| [huggingface/ml-intern](https://github.com/huggingface/ml-intern) | 5897 | Python | 🤗 ml-intern: an open-source ML engineer that reads papers, trains models, and ships ML models |

| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 495457 | Markdown | Master programming by recreating your favorite technologies from scratch. |
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
