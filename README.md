<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-08-16 00:41 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [cordiverse/cordis](https://github.com/cordiverse/cordis) | 4066 | TypeScript | Meta-Framework of Spatiotemporal Composability |

| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 18611 | HTML | 29 editorial diagram types for Claude Code. Self-contained HTML + SVG. No shadows, no Mermaid-slop. |

| [cursor/plugins](https://github.com/cursor/plugins) | 2950 | TypeScript | Cursor plugin specification and official plugins |

| [cactus-compute/needle](https://github.com/cactus-compute/needle) | 6063 | Python | 14MB foundation model for tiny devices; phones, wearables, smart home, and robots. |

| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 72047 | Python | Local UI to run and train LLMs and diffusion models, including Qwen3.8, Kimi K3, MiniMax-H3, Gemma 4, DeepSeek-V4, FLUX and more. |

| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 460168 | Python | A collective list of free APIs |

| [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) | 1659 | Python | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU. |

| [github/spec-kit](https://github.com/github/spec-kit) | 129196 | Python | 💫 Toolkit to help you get started with Spec-Driven Development |

| [megadose/holehe](https://github.com/megadose/holehe) | 13115 | Python | holehe allows you to check if the mail is used on different sites like twitter, instagram and will retrieve information on sites with the forgotten password function. |

| [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | 10326 | Swift | Fastest and only macOS Dictation app with on-device STT and custom trained AI enhancement model. A local Wispr Flow alternative. DM us on X for an easter egg 😉 - https://x.com/fluidvoiceapp |
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
