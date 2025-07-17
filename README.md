<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-07-17 01:00 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 64986 | Python | Python tool for converting files and office documents to Markdown. |

| [PromtEngineer/localGPT](https://github.com/PromtEngineer/localGPT) | 21060 | Python | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private. |

| [maotoumao/MusicFree](https://github.com/maotoumao/MusicFree) | 18193 | TypeScript | 插件化、定制化、无广告的免费音乐播放器 |

| [frappe/erpnext](https://github.com/frappe/erpnext) | 26813 | Python | Free and Open Source Enterprise Resource Planning (ERP) |

| [arc53/DocsGPT](https://github.com/arc53/DocsGPT) | 16086 | TypeScript | DocsGPT is an open-source genAI tool that helps users get reliable answers from knowledge source, while avoiding hallucinations. It enables private and reliable information retrieval, with tooling and agentic system capability built in. |

| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 23716 | PowerShell | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |

| [OpenPipe/ART](https://github.com/OpenPipe/ART) | 2658 | Python | Agent Reinforcement Trainer: train multi-step agents for real-world tasks using GRPO. Give your agents on-the-job training. Reinforcement learning for Qwen2.5, Qwen3, Llama, Kimi, and more! |

| [aws/amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli) | 1143 | Rust | ✨ Agentic chat experience in your terminal. Build applications using natural language. |

| [vpnhood/VpnHood](https://github.com/vpnhood/VpnHood) | 1498 | C# | Undetectable Fast Portable VPN |

| [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) | 6428 | Python | Build effective agents using Model Context Protocol and simple workflow patterns |
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
