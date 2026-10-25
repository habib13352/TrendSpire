<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-10-25 02:19 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 44696 | JavaScript | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings |

| [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | 19510 | Rust | OpenShell is the safe, private runtime for autonomous AI agents. |

| [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | 3149 | Python | Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS |

| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 32214 | CSS | Anti-AI-slop design skill for Claude Code, Cursor, and Codex. |

| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | 44601 | Python | A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value. |

| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 86468 | Rust | The design language that makes your AI harness better at design. |

| [pollen-robotics/microduck](https://github.com/pollen-robotics/microduck) | 11030 | Rust | A Tiny biped duck robot 🦆 |

| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 108095 | TypeScript | An open-source AI agent that brings the power of Gemini directly into your terminal. |

| [jbiaojerry/ebook-treasure-chest](https://github.com/jbiaojerry/ebook-treasure-chest) | 22669 | Python | 欢迎来到电子书下载宝库，一个汇聚了各类电子书下载链接的地方。无论你是喜欢阅读经典文学、经管励志、终身学习、职场创业、技术手册还是其他类型的书籍，这里都能满足你的需求。 该库涵盖了帆书app(原樊登读书)、微信读书、京东读书、喜马拉雅等读书app的大部分电子书。 |

| [makecindy/cindy](https://github.com/makecindy/cindy) | 4132 | TypeScript | Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。 |
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
