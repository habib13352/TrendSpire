<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-18 00:50 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 29147 | Python | 🚀🚀 「大模型」2小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 2h! |

| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | 88243 | Shell | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |

| [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | 341038 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |

| [dockur/windows](https://github.com/dockur/windows) | 47505 | Shell | Windows inside a Docker container. |

| [HuLaSpark/HuLa](https://github.com/HuLaSpark/HuLa) | 3986 | Vue | 🍀 A cross-platform instant messaging desktop application with exceptional performance built on Rust + Vue3, compatible with Windows, macOS, Linux, Android, and iOS（一款基于Rust+Vue3极致性能的跨平台即时通讯桌面应用，兼容Windows、MacOS、Linux、Android、IOS）🎉 10月20号 3.0版本重磅发布，敬请期待🎉 |

| [reflex-dev/reflex](https://github.com/reflex-dev/reflex) | 26647 | Python | 🕸️ Web apps in pure Python 🐍 |

| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 5157 | Python | An Open Source implementation of Notebook LM with more flexibility and features |

| [stamparm/maltrail](https://github.com/stamparm/maltrail) | 7496 | Python | Malicious traffic detection system |

| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 31026 | Unknown | leaked prompts of GPTs |

| [keycloak/keycloak](https://github.com/keycloak/keycloak) | 30331 | Java | Open Source Identity and Access Management For Modern Applications and Services |
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
