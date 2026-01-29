<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-01-29 01:11 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [moltbot/moltbot](https://github.com/moltbot/moltbot) | 88822 | TypeScript | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 |

| [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | 3138 | TypeScript | AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods |

| [hashicorp/vault](https://github.com/hashicorp/vault) | 34377 | Go | A tool for secrets management, encryption as a service, and privileged access management |

| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 26588 | JavaScript | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |

| [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | 5530 | Python | Memory for 24/7 proactive agents like moltbot (clawdbot). |

| [modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps) | 662 | TypeScript | Official repo for spec & SDK of MCP Apps protocol - standard for UIs embedded AI chatbots, served by MCP servers |

| [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | 4555 | Python | Kimi Code CLI is your next CLI agent. |

| [kubernetes/ingress-nginx](https://github.com/kubernetes/ingress-nginx) | 19353 | Go | Ingress NGINX Controller for Kubernetes |

| [protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf) | 70449 | C++ | Protocol Buffers - Google's data interchange format |

| [lobehub/lobehub](https://github.com/lobehub/lobehub) | 70898 | TypeScript | The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction. |
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
