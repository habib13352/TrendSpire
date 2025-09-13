<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-09-13 00:47 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [trueadm/ripple](https://github.com/trueadm/ripple) | 3720 | JavaScript | the elegant TypeScript UI framework |

| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 7092 | Python | No description provided. |

| [CodebuffAI/codebuff](https://github.com/CodebuffAI/codebuff) | 1166 | TypeScript | Generate code from the terminal! |

| [sentient-agi/ROMA](https://github.com/sentient-agi/ROMA) | 1648 | Python | Recursive-Open-Meta-Agent v0.1 (Beta). A meta-agent framework to build high-performance multi-agent systems. |

| [firebase/genkit](https://github.com/firebase/genkit) | 3153 | TypeScript | An open source framework for building AI-powered apps with familiar code-centric patterns. Genkit makes it easy to develop, integrate, and test AI features with observability and evaluations. Genkit works with various models and platforms. |

| [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | 29071 | HTML | all of the workflows of n8n i could find (also from the site itself) |

| [epfml/ML_course](https://github.com/epfml/ML_course) | 1617 | Jupyter Notebook | EPFL Machine Learning Course, Fall 2025 |

| [expo/expo](https://github.com/expo/expo) | 43204 | TypeScript | An open-source framework for making universal native apps with React. Expo runs on Android, iOS, and the web. |

| [NVIDIA/garak](https://github.com/NVIDIA/garak) | 5453 | Python | the LLM vulnerability scanner |

| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 37221 | Go | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search |
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
