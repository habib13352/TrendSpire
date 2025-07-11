<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-07-11 00:59 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [Alibaba-NLP/WebAgent](https://github.com/Alibaba-NLP/WebAgent) | 3255 | Python | 🌐 WebAgent for Information Seeking bulit by Tongyi Lab: WebWalker & WebDancer & WebSailor https://arxiv.org/pdf/2507.02592 |

| [WordPress/wordpress-develop](https://github.com/WordPress/wordpress-develop) | 2868 | PHP | WordPress Develop, Git-ified. Synced from git://develop.git.wordpress.org/, including branches and tags! This repository is just a mirror of the WordPress subversion repository. Please include a link to a pre-existing ticket on https://core.trac.wordpress.org/ with every pull request. |

| [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) | 4928 | Go | MCP Toolbox for Databases is an open source MCP server for databases. |

| [LMCache/LMCache](https://github.com/LMCache/LMCache) | 2832 | Python | Supercharge Your LLM with the Fastest KV Cache Layer |

| [forthespada/CS-Books](https://github.com/forthespada/CS-Books) | 23641 | Unknown | 🔥🔥超过1000本的计算机经典书籍、个人笔记资料以及本人在各平台发表文章中所涉及的资源等。书籍资源包括C/C++、Java、Python、Go语言、数据结构与算法、操作系统、后端架构、计算机系统知识、数据库、计算机网络、设计模式、前端、汇编以及校招社招各种面经~ |

| [ByteByteGoHq/system-design-101](https://github.com/ByteByteGoHq/system-design-101) | 74200 | Unknown | Explain complex systems using visuals and simple terms. Help you prepare for system design interviews. |

| [snap-stanford/Biomni](https://github.com/snap-stanford/Biomni) | 1000 | Python | Biomni: a general-purpose biomedical AI agent |

| [pybind/pybind11](https://github.com/pybind/pybind11) | 16859 | C++ | Seamless operability between C++11 and Python |

| [punkpeye/awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients) | 4552 | Unknown | A collection of MCP clients. |

| [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | 12237 | Python | Automate the process of making money online. |
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
