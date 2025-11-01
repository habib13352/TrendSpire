<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-11-01 12:25 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [get-convex/chef](https://github.com/get-convex/chef) | 2548 | TypeScript | The only AI app builder that knows backend |

| [suitenumerique/docs](https://github.com/suitenumerique/docs) | 14101 | Python | A collaborative note taking, wiki and documentation platform that scales. Built with Django and React. |

| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 7085 | Go | LLM-powered framework for deep document understanding, semantic retrieval, and context-aware answers using RAG paradigm. |

| [janhq/jan](https://github.com/janhq/jan) | 38864 | TypeScript | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer. |

| [microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners) | 93602 | JavaScript | 24 Lessons, 12 Weeks, Get Started as a Web Developer |

| [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | 74587 | Python | real time face swap and one-click video deepfake with only a single image |

| [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | 38788 | Rust | An open source payments switch written in Rust to make payments fast, reliable and affordable |

| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | 88793 | Shell | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |

| [github/copilot-cli](https://github.com/github/copilot-cli) | 4396 | Unknown | GitHub Copilot CLI brings the power of Copilot coding agent directly to your terminal. |

| [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | 33845 | Java | 🔥 官方推荐 🔥 RuoYi-Vue 全新 Pro 版本，优化重构所有功能。基于 Spring Boot + MyBatis Plus + Vue & Element 实现的后台管理系统 + 微信小程序，支持 RBAC 动态权限、数据权限、SaaS 多租户、Flowable 工作流、三方登录、支付、短信、商城、CRM、ERP、AI 大模型等功能。你的 ⭐️ Star ⭐️，是作者生发的动力！ |
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
