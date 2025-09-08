<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-09-08 12:29 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [emcie-co/parlant](https://github.com/emcie-co/parlant) | 10530 | Python | LLM agents built for control. Designed for real-world use. Deployed in minutes. |

| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 36652 | Jupyter Notebook | 11 Lessons to Get Started Building AI Agents |

| [zama-ai/fhevm](https://github.com/zama-ai/fhevm) | 17681 | Rust | FHEVM, a full-stack framework for integrating Fully Homomorphic Encryption (FHE) with blockchain applications |

| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | 18344 | TypeScript | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra |

| [openwrt/openwrt](https://github.com/openwrt/openwrt) | 23703 | C | This repository is a mirror of https://git.openwrt.org/openwrt/openwrt.git It is for reference only and is not active for check-ins. We will continue to accept Pull Requests here. They will be merged via staging trees then into openwrt.git. |

| [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | 9056 | TypeScript | Open Source AI coding assistant for planning, building, and fixing code. We frequently merge features from open-source projects like Roo Code and Cline, while building our own vision. Follow us: kilocode.ai/social |

| [11cafe/jaaz](https://github.com/11cafe/jaaz) | 2665 | TypeScript | The world's first open-source multimodal creative assistant This is a substitute for Canva and Manus that prioritizes privacy and is usable locally. |

| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 81688 | Unknown | FULL v0, Cursor, Manus, Augment Code, Same.dev, Lovable, Devin, Replit Agent, Windsurf Agent, VSCode Agent, Dia Browser, Xcode, Trae AI, Cluely & Orchids.app (And other Open Sourced) System Prompts, Tools & AI Models. |

| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 97057 | Jupyter Notebook | 21 Lessons, Get Started Building with Generative AI |

| [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) | 65769 | Java | #1 Locally hosted web application that allows you to perform various operations on PDF files |
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
