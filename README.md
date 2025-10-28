<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-28 12:28 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 57748 | TypeScript | There can be more than Notion and Miro. AFFiNE(pronounced [ə‘fain]) is a next-gen knowledge base that brings planning, sorting and creating all together. Privacy first, open-source, customizable and ready to use. |

| [yeongpin/cursor-free-vip](https://github.com/yeongpin/cursor-free-vip) | 38994 | Python | [Support 0.49.x]（Reset Cursor AI MachineID & Bypass Higher Token Limit） Cursor Ai ，自动重置机器ID ， 免费升级使用Pro功能: You've reached your trial request limit. / Too many free trial accounts used on this machine. Please upgrade to pro. We have this limit in place to prevent abuse. Please let us know if you believe this is a mistake. |

| [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | 3089 | Python | The absolute trainer to light up AI agents. |

| [spipm/Depixelization_poc](https://github.com/spipm/Depixelization_poc) | 2008 | Python | Depix is a PoC for a technique to recover plaintext from pixelized screenshots. |

| [longbridge/gpui-component](https://github.com/longbridge/gpui-component) | 5695 | Rust | Rust GUI components for building fantastic cross-platform desktop application by using GPUI. |

| [juanfont/headscale](https://github.com/juanfont/headscale) | 32027 | Go | An open source, self-hosted implementation of the Tailscale control server |

| [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | 6834 | Python | Introduction to Machine Learning Systems |

| [qeeqbox/social-analyzer](https://github.com/qeeqbox/social-analyzer) | 14744 | JavaScript | API, CLI, and Web App for analyzing and finding a person's profile in 1000 social media \ websites |

| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | 19098 | Jupyter Notebook | In-depth tutorials on LLMs, RAGs and real-world AI agent applications. |

| [cloudcommunity/Free-Certifications](https://github.com/cloudcommunity/Free-Certifications) | 41028 | Unknown | A curated list of free courses with certifications. Also available at https://free-certifications.com/ |
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
