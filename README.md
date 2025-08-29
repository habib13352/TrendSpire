<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-08-29 12:27 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [QuentinFuxa/WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit) | 2079 | Python | Real-time & local speech-to-text, translation, and speaker diarization. With server & web UI. |

| [microsoft/mcp](https://github.com/microsoft/mcp) | 637 | C# | Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration |

| [Canner/WrenAI](https://github.com/Canner/WrenAI) | 10628 | TypeScript | ⚡️ GenBI (Generative BI) queries any database in natural language, generates accurate SQL (Text-to-SQL), charts (Text-to-Chart), and AI-powered insights in seconds. |

| [OpenBMB/MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | 20378 | Python | MiniCPM-V 4.5: A GPT-4o Level MLLM for Single Image, Multi Image and Video Understanding on Your Phone |

| [twbs/bootstrap](https://github.com/twbs/bootstrap) | 173183 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |

| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 204989 | Python | All Algorithms implemented in Python |

| [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | 1335 | TypeScript | HumanLayer enables AI agents to communicate with humans in tool-based and async workflows. Guarantee human oversight of high-stakes function calls with approval workflows across slack, email and more. Bring your LLM and Framework of choice and start giving your AI agents safe access to the world. Agentic Workflows, human in the loop, tool calling |

| [nats-io/nats-server](https://github.com/nats-io/nats-server) | 17925 | Go | High-Performance server for NATS.io, the cloud and edge native messaging system. |

| [spf13/cobra](https://github.com/spf13/cobra) | 41668 | Go | A Commander for modern Go CLI interactions |

| [microsoft/terminal](https://github.com/microsoft/terminal) | 99648 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |
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
