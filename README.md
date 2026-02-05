<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2026-02-05 12:47 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | 26460 | TypeScript | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra |

| [openai/skills](https://github.com/openai/skills) | 4028 | Python | Skills Catalog for Codex |

| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 23345 | TypeScript | A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. |

| [j178/prek](https://github.com/j178/prek) | 5347 | Rust | ⚡ Better `pre-commit`, re-engineered in Rust |

| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 11723 | Python | Memory for AI Agents in 6 lines of code |

| [obra/superpowers](https://github.com/obra/superpowers) | 44975 | Shell | An agentic skills framework & software development methodology that works. |

| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | 31285 | Go | Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more |

| [fish-shell/fish-shell](https://github.com/fish-shell/fish-shell) | 32284 | Rust | The user-friendly command line shell. |

| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | 91317 | Shell | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |

| [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | 19240 | TypeScript | 一款提示词优化器，助力于编写高质量的提示词 |
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
