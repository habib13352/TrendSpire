<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-06-09 12:28 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [alphacep/vosk-api](https://github.com/alphacep/vosk-api) | 10344 | Jupyter Notebook | Offline speech recognition API for Android, iOS, Raspberry Pi and servers with Python, Java, C# and Node |

| [tensorzero/tensorzero](https://github.com/tensorzero/tensorzero) | 5782 | Rust | TensorZero creates a feedback loop for optimizing LLM applications — turning production data into smarter, faster, and cheaper models. |

| [XTLS/Xray-core](https://github.com/XTLS/Xray-core) | 28988 | Go | Xray, Penetrates Everything. Also the best v2ray-core. Where the magic happens. An open platform for various uses. |

| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 4836 | Python | Memory for AI Agents in 5 lines of code |

| [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | 13107 | JavaScript | An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others. |

| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 17004 | Jupyter Notebook | This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. RAG systems combine information retrieval with generative models to provide accurate and contextually rich responses. |

| [eythaann/Seelen-UI](https://github.com/eythaann/Seelen-UI) | 7261 | Rust | The Fully Customizable Desktop Environment for Windows 10/11. |

| [zijie0/HumanSystemOptimization](https://github.com/zijie0/HumanSystemOptimization) | 15978 | Unknown | 健康学习到150岁 - 人体系统调优不完全指南 |

| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 57092 | MDX | 🐙 Guides, papers, lecture, notebooks and resources for prompt engineering |

| [PathOfBuildingCommunity/PathOfBuilding](https://github.com/PathOfBuildingCommunity/PathOfBuilding) | 4622 | Lua | Offline build planner for Path of Exile. |
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
