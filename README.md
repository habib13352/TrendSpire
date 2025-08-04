<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-08-04 01:06 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | 4916 | TypeScript | Free, local, open-source AI app builder | v0 / lovable / Bolt alternative | 🌟 Star if you like it! |

| [wg-easy/wg-easy](https://github.com/wg-easy/wg-easy) | 21074 | TypeScript | The easiest way to run WireGuard VPN + Web-based Admin UI. |

| [eclipse-sumo/sumo](https://github.com/eclipse-sumo/sumo) | 3329 | C++ | Eclipse SUMO is an open source, highly portable, microscopic and continuous traffic simulation package designed to handle large networks. It allows for intermodal simulation including pedestrians and comes with a large set of tools for scenario creation. |

| [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) | 192720 | JavaScript | 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings |

| [XTLS/Xray-core](https://github.com/XTLS/Xray-core) | 30383 | Go | Xray, Penetrates Everything. Also the best v2ray-core. Where the magic happens. An open platform for various uses. |

| [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin) | 41870 | C# | The Free Software Media System - Server Backend & API |

| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 61360 | Jupyter Notebook | Implement a ChatGPT-like LLM in PyTorch from scratch, step by step |

| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | 46296 | C++ | Truly independent web browser |

| [sst/opencode](https://github.com/sst/opencode) | 16750 | Go | AI coding agent, built for the terminal. |

| [TideDra/zotero-arxiv-daily](https://github.com/TideDra/zotero-arxiv-daily) | 2646 | Python | Recommend new arxiv papers of your interest daily according to your Zotero libarary. |
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
