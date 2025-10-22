<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-22 12:29 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [mountain-loop/yaak](https://github.com/mountain-loop/yaak) | 11196 | TypeScript | The most intuitive desktop API client. Organize and execute REST, GraphQL, WebSockets, Server Sent Events, and gRPC 🦬 |

| [servo/servo](https://github.com/servo/servo) | 32670 | Rust | Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications. |

| [emcie-co/parlant](https://github.com/emcie-co/parlant) | 14045 | Python | LLM agents built for control. Designed for real-world use. Deployed in minutes. |

| [guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark) | 7582 | Python | Blind&Invisible Watermark ，图片盲水印，提取水印无须原图！ |

| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 7050 | TypeScript | An Open Source implementation of Notebook LM with more flexibility and features |

| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | 16633 | TypeScript | Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it! |

| [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | 23375 | Python | SOTA Open Source TTS |

| [huggingface/chat-ui](https://github.com/huggingface/chat-ui) | 9890 | TypeScript | Open source codebase powering the HuggingChat app |

| [rossant/awesome-math](https://github.com/rossant/awesome-math) | 10266 | Python | A curated list of awesome mathematics resources |

| [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | 33415 | JavaScript | Free, simple, and intuitive online database diagram editor and SQL generator. |
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
