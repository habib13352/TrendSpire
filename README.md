<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-12-07 01:03 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | 11055 | Python | Open-Source Frontier Voice AI |

| [rustfs/rustfs](https://github.com/rustfs/rustfs) | 15137 | Rust | 🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph. |

| [RosettaCommons/foundry](https://github.com/RosettaCommons/foundry) | 415 | Python | Central repository for biomolecular foundation models with shared trainers and pipeline components |

| [sinelaw/fresh](https://github.com/sinelaw/fresh) | 821 | Rust | Text editor for your terminal: easy, powerful and fast |

| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | 21424 | Jupyter Notebook | In-depth tutorials on LLMs, RAGs and real-world AI agent applications. |

| [psviderski/uncloud](https://github.com/psviderski/uncloud) | 3836 | Go | A lightweight tool for deploying and managing containerised applications across a network of Docker hosts. Bridging the gap between Docker and Kubernetes ✨ |

| [oven-sh/bun](https://github.com/oven-sh/bun) | 84387 | Zig | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |

| [facebook/react](https://github.com/facebook/react) | 241316 | JavaScript | The library for web and native user interfaces. |

| [lynx-family/lynx](https://github.com/lynx-family/lynx) | 13774 | C++ | Empower the Web community and invite more to build across platforms. |

| [DevCaress/guia-entrevistas-de-programacion](https://github.com/DevCaress/guia-entrevistas-de-programacion) | 6704 | Unknown | No description provided. |
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
