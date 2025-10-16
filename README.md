<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-16 00:53 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 23875 | Jupyter Notebook | Anthropic's Interactive Prompt Engineering Tutorial |

| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 27654 | Python | 🚀🚀 「大模型」2小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 2h! |

| [nitrojs/nitro](https://github.com/nitrojs/nitro) | 8821 | TypeScript | Next Generation Server Toolkit. Create web servers with everything you need and deploy them wherever you prefer. |

| [langchain-ai/langchainjs](https://github.com/langchain-ai/langchainjs) | 15944 | TypeScript | 🦜🔗 Build context-aware reasoning applications 🦜🔗 |

| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | 45821 | Python | The simplest, fastest repository for training/finetuning medium-sized GPTs. |

| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | 87610 | Shell | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |

| [envoyproxy/envoy](https://github.com/envoyproxy/envoy) | 26732 | C++ | Cloud-native high-performance edge/middle/service proxy |

| [EvolutionAPI/evolution-api](https://github.com/EvolutionAPI/evolution-api) | 5808 | TypeScript | Evolution API is an open-source WhatsApp integration API |

| [devlikeapro/waha](https://github.com/devlikeapro/waha) | 4666 | TypeScript | WAHA - WhatsApp HTTP API (REST API) that you can configure in a click! 3 engines: WEBJS (browser based), NOWEB (websocket nodejs), GOWS (websocket go) |

| [enactic/openarm](https://github.com/enactic/openarm) | 1200 | MDX | A fully open-source humanoid arm for physical AI research and deployment in contact-rich environments. |
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
