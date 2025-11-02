<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-11-02 12:24 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | 3857 | Python | 微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。 |

| [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | 4768 | JavaScript | CRS-自建Claude Code镜像，一站式开源中转服务，让 Claude、OpenAI、Gemini、Droid 订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。 |

| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | 5862 | Python | The absolute trainer to light up AI agents. |

| [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) | 8241 | Python | "DeepCode: Open Agentic Coding (Paper2Code & Text2Web & Text2Backend)" |

| [GeeeekExplorer/nano-vllm](https://github.com/GeeeekExplorer/nano-vllm) | 7426 | Python | Nano vLLM |

| [sst/opencode](https://github.com/sst/opencode) | 30285 | TypeScript | The AI coding agent built for the terminal. |

| [charmbracelet/glow](https://github.com/charmbracelet/glow) | 19891 | Go | Render markdown on the CLI, with pizzazz! 💅🏻 |

| [NARKOZ/hacker-scripts](https://github.com/NARKOZ/hacker-scripts) | 48983 | JavaScript | Based on a true story |

| [moondevonyt/moon-dev-ai-agents](https://github.com/moondevonyt/moon-dev-ai-agents) | 2263 | Python | autonomous ai agents for trading in python |

| [suitenumerique/docs](https://github.com/suitenumerique/docs) | 14276 | Python | A collaborative note taking, wiki and documentation platform that scales. Built with Django and React. |
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
