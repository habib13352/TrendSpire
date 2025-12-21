<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-12-21 01:03 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [exo-explore/exo](https://github.com/exo-explore/exo) | 34561 | Python | Run your own AI cluster at home with everyday devices 📱💻 🖥️⌚ |

| [lintsinghua/DeepAudit](https://github.com/lintsinghua/DeepAudit) | 2036 | Python | DeepAudit：人人拥有的 AI 黑客战队，让漏洞挖掘触手可及。国内首个开源的代码漏洞挖掘多智能体系统。小白一键部署运行，自主协作审计 + 自动化沙箱 PoC 验证。支持 Ollama 私有部署 ，一键生成报告。​让安全不再昂贵，让审计不再复杂。 |

| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 47428 | Shell | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. |

| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 15044 | JavaScript | Community-contributed instructions, prompts, and configurations to help you make the most of GitHub Copilot. |

| [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | 72855 | Python | A list of useful payloads and bypass for Web Application Security and Pentest/CTF |

| [sgl-project/mini-sglang](https://github.com/sgl-project/mini-sglang) | 1702 | Python | No description provided. |

| [cloudcommunity/Free-Certifications](https://github.com/cloudcommunity/Free-Certifications) | 47164 | Unknown | A curated list of free courses with certifications. Also available at https://free-certifications.com/ |

| [GreyDGL/PentestGPT](https://github.com/GreyDGL/PentestGPT) | 9799 | Python | A GPT-empowered penetration testing tool |

| [NexaAI/nexa-sdk](https://github.com/NexaAI/nexa-sdk) | 6757 | Go | Run the latest LLMs and VLMs across GPU, NPU, and CPU with PC (Python/C++) & mobile (Android & iOS) support, running quickly with OpenAI gpt-oss, Granite4, Qwen3VL, Gemma 3n and more. |

| [astral-sh/ty](https://github.com/astral-sh/ty) | 15256 | Python | An extremely fast Python type checker and language server, written in Rust. |
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
