<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-06-08 12:25 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [tensorzero/tensorzero](https://github.com/tensorzero/tensorzero) | 4791 | Rust | TensorZero creates a feedback loop for optimizing LLM applications — turning production data into smarter, faster, and cheaper models. |

| [codexu/note-gen](https://github.com/codexu/note-gen) | 3770 | TypeScript | A cross-platform Markdown note-taking application dedicated to using AI to bridge recording and writing, organizing fragmented knowledge into a readable note. |

| [langgenius/dify](https://github.com/langgenius/dify) | 102080 | TypeScript | Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. |

| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 4430 | Python | Memory for AI Agents in 5 lines of code |

| [XTLS/Xray-core](https://github.com/XTLS/Xray-core) | 28839 | Go | Xray, Penetrates Everything. Also the best v2ray-core. Where the magic happens. An open platform for various uses. |

| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 33571 | Python | Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models. |

| [zijie0/HumanSystemOptimization](https://github.com/zijie0/HumanSystemOptimization) | 15110 | Unknown | 健康学习到150岁 - 人体系统调优不完全指南 |

| [iib0011/omni-tools](https://github.com/iib0011/omni-tools) | 2906 | TypeScript | Self-hosted collection of powerful web-based tools for everyday tasks. No ads, no tracking, just fast, accessible utilities right from your browser! |

| [netbirdio/netbird](https://github.com/netbirdio/netbird) | 15111 | Go | Connect your devices into a secure WireGuard®-based overlay network with SSO, MFA and granular access controls. |

| [Daymychen/art-design-pro](https://github.com/Daymychen/art-design-pro) | 1820 | Vue | A Vue 3 admin dashboard template using Vite + TypeScript + Element Plus | vue3 admin | vue-admin — focused on user experience and visual design. |
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
