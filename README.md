<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-07-20 12:28 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [srbhr/Resume-Matcher](https://github.com/srbhr/Resume-Matcher) | 9474 | TypeScript | Improve your resumes with Resume Matcher. Get insights, keyword suggestions and tune your resumes to job descriptions. |

| [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) | 27953 | C++ | Hyprland is an independent, highly customizable, dynamic tiling Wayland compositor that doesn't sacrifice on its looks. |

| [better-auth/better-auth](https://github.com/better-auth/better-auth) | 16605 | TypeScript | The most comprehensive authentication framework for TypeScript |

| [remoteintech/remote-jobs](https://github.com/remoteintech/remote-jobs) | 33155 | JavaScript | A list of semi to fully remote-friendly companies (jobs) in tech. |

| [maybe-finance/maybe](https://github.com/maybe-finance/maybe) | 47165 | Ruby | The personal finance app for everyone |

| [simstudioai/sim](https://github.com/simstudioai/sim) | 5122 | TypeScript | Sim Studio is an open-source AI agent workflow builder. Sim Studio's interface is a lightweight, intuitive way to quickly build and deploy LLMs that connect with your favorite tools. |

| [roboflow/supervision](https://github.com/roboflow/supervision) | 27650 | Python | We write your reusable computer vision tools. 💜 |

| [shadps4-emu/shadPS4](https://github.com/shadps4-emu/shadPS4) | 24702 | C++ | PlayStation 4 emulator for Windows, Linux and macOS written in C++ |

| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) | 5394 | Python | No description provided. |

| [tracel-ai/burn](https://github.com/tracel-ai/burn) | 11715 | Rust | Burn is a next generation Deep Learning Framework that doesn't compromise on flexibility, efficiency and portability. |
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
