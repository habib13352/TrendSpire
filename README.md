<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-19 12:25 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | 21546 | Jupyter Notebook | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |

| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 5455 | TypeScript | An Open Source implementation of Notebook LM with more flexibility and features |

| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 30093 | Python | 🚀🚀 「大模型」2小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 2h! |

| [atuinsh/desktop](https://github.com/atuinsh/desktop) | 1614 | TypeScript | 📖 Runbooks that run |

| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 373253 | Python | 📚 Freely available programming books |

| [mountain-loop/yaak](https://github.com/mountain-loop/yaak) | 8245 | TypeScript | The most intuitive desktop API client. Organize and execute REST, GraphQL, WebSockets, Server Sent Events, and gRPC 🦬 |

| [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) | 14661 | Python | Automate browser-based workflows with LLMs and Computer Vision |

| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 58636 | Python | Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages. |

| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 211307 | Python | All Algorithms implemented in Python |

| [ThinkInAIXYZ/deepchat](https://github.com/ThinkInAIXYZ/deepchat) | 4443 | TypeScript | 🐬DeepChat - A smart assistant that connects powerful AI to your personal world |
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
