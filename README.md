<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-09-24 00:52 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [gin-gonic/gin](https://github.com/gin-gonic/gin) | 84221 | Go | Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices. |

| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | 48331 | C++ | Truly independent web browser |

| [gofiber/fiber](https://github.com/gofiber/fiber) | 37776 | Go | ⚡️ Express inspired web framework written in Go |

| [eslint/eslint](https://github.com/eslint/eslint) | 26444 | JavaScript | Find and fix problems in your JavaScript code. |

| [fmtlib/fmt](https://github.com/fmtlib/fmt) | 22534 | C++ | A modern formatting library |

| [mtdvio/every-programmer-should-know](https://github.com/mtdvio/every-programmer-should-know) | 90701 | Unknown | A collection of (mostly) technical things every software developer should know about |

| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | 87056 | Shell | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions |

| [OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) | 26382 | Solidity | OpenZeppelin Contracts is a library for secure smart contract development. |

| [Gar-b-age/CookLikeHOC](https://github.com/Gar-b-age/CookLikeHOC) | 17351 | JavaScript | 🥢像老乡鸡🐔那样做饭。主要部分于2024年完工，非老乡鸡官方仓库。文字来自《老乡鸡菜品溯源报告》，并做归纳、编辑与整理。CookLikeHOC. |

| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 370067 | Python | 📚 Freely available programming books |
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
