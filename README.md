<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-07-26 12:27 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [frappe/hrms](https://github.com/frappe/hrms) | 4436 | Python | Open Source HR and Payroll Software |

| [QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) | 9123 | Python | Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team, Alibaba Cloud. |

| [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | 22803 | Rust | An open source payments switch written in Rust to make payments fast, reliable and affordable |

| [m1k1o/neko](https://github.com/m1k1o/neko) | 13865 | Go | A self hosted virtual browser that runs in docker and uses WebRTC. |

| [aaPanel/BillionMail](https://github.com/aaPanel/BillionMail) | 7847 | Go | BillionMail gives you open-source MailServer, NewsLetter, Email Marketing — fully self-hosted, dev-friendly, and free from monthly fees. Join the discord: https://discord.gg/asfXzBUhZr |

| [keycloak/keycloak](https://github.com/keycloak/keycloak) | 28493 | Java | Open Source Identity and Access Management For Modern Applications and Services |

| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 26169 | Python | Python SDK, Proxy Server (LLM Gateway) to call 100+ LLM APIs in OpenAI format - [Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, Replicate, Groq] |

| [Infisical/infisical](https://github.com/Infisical/infisical) | 18970 | TypeScript | Infisical is the open-source platform for secrets management, PKI, and SSH access. |

| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | 9439 | Python | The LLM Evaluation Framework |

| [dataease/dataease](https://github.com/dataease/dataease) | 20725 | Java | 🔥 人人可用的开源 BI 工具，数据可视化神器。An open-source BI tool alternative to Tableau. |
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
