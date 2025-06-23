<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-06-23 01:01 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 53187 | Jupyter Notebook | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step |

| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | 11459 | Jupyter Notebook | In-depth tutorials on LLMs, RAGs and real-world AI agent applications. |

| [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | 32740 | Python | A community-maintained Python framework for creating mathematical animations. |

| [microsoft/edit](https://github.com/microsoft/edit) | 9016 | Rust | We all edit. |

| [mikumifa/biliTickerBuy](https://github.com/mikumifa/biliTickerBuy) | 2109 | Python | b站会员购购票辅助工具 |

| [kortix-ai/suna](https://github.com/kortix-ai/suna) | 15347 | TypeScript | Suna - Open Source Generalist AI Agent |

| [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | 26407 | Java | Telegram for Android source |

| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 14460 | Shell | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |

| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | 33553 | Jupyter Notebook | This is a repo with links to everything you'd ever want to learn about data engineering |

| [cyclotruc/gitingest](https://github.com/cyclotruc/gitingest) | 9910 | Python | Replace 'hub' with 'ingest' in any github url to get a prompt-friendly extract of a codebase |
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

Another workflow [`ai_loop.yml`](.github/workflows/ai_loop.yml) drives the Codex automation using [`ai_loop/trendspire_autoloop.py`](ai_loop/trendspire_autoloop.py). It supports two modes:

- **Daily** – diff-based improvements using `gpt-3.5-turbo`.
- **Weekly** – a full repository review with `gpt-4o`.

Each run applies the returned diff, executes the test suite and, when successful, creates a branch and pull request. Summaries, cost logs and the raw diff are saved under `codex_logs/` and uploaded as workflow artifacts. The workflow also caches the `trendspire_memory/` directory so the AI can refine its suggestions over time.

To run the Codex automation locally you can execute:

```bash
python ai_loop/trendspire_autoloop.py --mode daily   # or weekly
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
