<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-10-22 02:28 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 36693 | JavaScript | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings |

| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 94914 | Python | A high-throughput and memory-efficient inference and serving engine for LLMs |

| [stablyai/orca](https://github.com/stablyai/orca) | 101415 | TypeScript | Orca is the place for working with a fleet of agents (e.g. Grok Bot, Claude Code). Run any coding agent with your own subscription. Available on desktop, mobile and remote runtime. |

| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 77300 | Python | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server. |

| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 171790 | JavaScript | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. |

| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 141579 | Python | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. The fastest local inference engine in the world. |

| [supabase/supabase](https://github.com/supabase/supabase) | 113051 | TypeScript | The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications. |

| [twentyhq/twenty](https://github.com/twentyhq/twenty) | 59219 | TypeScript | The open alternative to Salesforce, designed for AI. |

| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | 42870 | Python | Kronos: A Foundation Model for the Language of Financial Markets |

| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | 12379 | Rust | Solution for long term memory for agent coding CLIs and to facilitate handoff between different agent vendors |
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
