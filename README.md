<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-25 00:52 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | 51441 | C++ | Truly independent web browser |

| [guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark) | 9627 | Python | Blind&Invisible Watermark ，图片盲水印，提取水印无须原图！ |

| [hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch) | 75676 | TypeScript | Open source API development ecosystem - https://hoppscotch.io (open-source alternative to Postman, Insomnia) |

| [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr) | 13401 | C | Primary Git Repository for the Zephyr Project. Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures. |

| [minio/minio](https://github.com/minio/minio) | 57141 | Go | MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license. |

| [emcie-co/parlant](https://github.com/emcie-co/parlant) | 14633 | Python | LLM agents built for control. Designed for real-world use. Deployed in minutes. |

| [zyronon/TypeWords](https://github.com/zyronon/TypeWords) | 4572 | Vue | 练习英语，一次敲击，一点进步；Practice English, one strike, one step forward |

| [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | 33371 | Python | A community-supported supercharged document management system: scan, index and archive all your documents |

| [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | 50476 | C# | PowerShell for every system! |

| [Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video) | 8434 | Python | Official repository for LTX-Video |
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
