<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-15 00:53 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 22863 | Jupyter Notebook | Anthropic's Interactive Prompt Engineering Tutorial |

| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | 87478 | Shell | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |

| [GorvGoyl/Clone-Wars](https://github.com/GorvGoyl/Clone-Wars) | 30388 | Unknown | 100+ open-source clones of popular sites like Airbnb, Amazon, Instagram, Netflix, Tiktok, Spotify, Whatsapp, Youtube etc. See source code, demo links, tech stack, github stars. |

| [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | 6265 | Java | Agentic AI Framework for Java Developers |

| [datawhalechina/happy-llm](https://github.com/datawhalechina/happy-llm) | 19439 | Jupyter Notebook | 📚 从零开始的大语言模型原理与实践教程 |

| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 22637 | JavaScript | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |

| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | 46325 | Python | Transforms complex documents like PDFs into LLM-ready markdown/JSON for your Agentic workflows. |

| [nitrojs/nitro](https://github.com/nitrojs/nitro) | 8487 | TypeScript | Next Generation Server Toolkit. Create web servers with everything you need and deploy them wherever you prefer. |

| [Klavis-AI/klavis](https://github.com/Klavis-AI/klavis) | 5152 | Python | Klavis AI (YC X25): MCP integration platforms that let AI agents use tools reliably at any scale |

| [chili-chips-ba/wireguard-fpga](https://github.com/chili-chips-ba/wireguard-fpga) | 1041 | Verilog | Full-throttle, wire-speed hardware implementation of Wireguard VPN, using low-cost Artix7 FPGA with opensource toolchain. If you seek security and privacy, nothing is private in our codebase. Our door is wide open for backdoor scrutiny, be it related to RTL, embedded, build, bitstream or any other aspect of design and delivery package. Bujrum! |
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
