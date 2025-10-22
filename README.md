<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-10-22 00:55 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [mountain-loop/yaak](https://github.com/mountain-loop/yaak) | 10310 | TypeScript | The most intuitive desktop API client. Organize and execute REST, GraphQL, WebSockets, Server Sent Events, and gRPC 🦬 |

| [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) | 76476 | JavaScript | A fancy self-hosted monitoring tool |

| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 6755 | TypeScript | An Open Source implementation of Notebook LM with more flexibility and features |

| [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | 12905 | Python | Generate audiobooks from e-books, voice cloning & 1107+ languages! |

| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | 24333 | Jupyter Notebook | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude. |

| [sharkdp/bat](https://github.com/sharkdp/bat) | 55321 | Rust | A cat(1) clone with wings. |

| [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) | 15133 | Python | Automate browser-based workflows with LLMs and Computer Vision |

| [oceanbase/miniob](https://github.com/oceanbase/miniob) | 4108 | C++ | MiniOB is a compact database that assists developers in understanding the fundamental workings of a database. |

| [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | 7923 | C++ | Speech-to-text, text-to-speech, speaker diarization, speech enhancement, source separation, and VAD using next-gen Kaldi with onnxruntime without Internet connection. Support embedded systems, Android, iOS, HarmonyOS, Raspberry Pi, RISC-V, x86_64 servers, websocket server/client, support 12 programming languages |

| [servo/servo](https://github.com/servo/servo) | 32486 | Rust | Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications. |
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
