<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-05-19 02:26 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | 17571 | Rust | Your Personal AI super intelligence. Private, Simple and extremely powerful. |

| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 12001 | Python | Academic Research Skills for Claude Code: research → write → review → revise → finalize |

| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 36727 | Python | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ |

| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 24444 | Python | A set of ready to use Agent Skills for research, science, engineering, analysis, finance and writing. |

| [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | 8387 | Swift | Lightning-Fast, On-Device, Multilingual TTS — running natively via ONNX. |

| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 111083 | C++ | LLM inference in C/C++ |

| [ruvnet/RuView](https://github.com/ruvnet/RuView) | 59952 | Rust | π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all without a single pixel of video. |

| [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | 15330 | Python | Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed. |

| [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | 4084 | TypeScript | The secure, validated skill registry for professional AI coding agents. Extend Antigravity, Claude Code, Cursor, Copilot and more with absolute confidence. |

| [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | 7775 | Python | Open-source intelligence for the global theater. Track everything from the corporate/private jets of the wealthy, and spy satellites, to seismic events in one unified interface. Hook an AI agent up to have it parse through data and find previously unseen correlations. The knowledge is available to all but rarely aggregated in the open, until now. |
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
