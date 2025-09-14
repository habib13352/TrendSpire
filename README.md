<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-09-14 00:55 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | 48942 | C# | PowerShell for every system! |

| [trueadm/ripple](https://github.com/trueadm/ripple) | 4196 | JavaScript | the elegant TypeScript UI framework |

| [MotiaDev/motia](https://github.com/MotiaDev/motia) | 8277 | TypeScript | Modern Backend Framework that unifies APIs, background jobs, workflows, and AI Agents into a single core primitive with built-in observability and state management. |

| [grpc/grpc-go](https://github.com/grpc/grpc-go) | 22272 | Go | The Go language implementation of gRPC. HTTP/2 based RPC |

| [sentient-agi/ROMA](https://github.com/sentient-agi/ROMA) | 1881 | Python | Recursive-Open-Meta-Agent v0.1 (Beta). A meta-agent framework to build high-performance multi-agent systems. |

| [ReVanced/revanced-patches](https://github.com/ReVanced/revanced-patches) | 4349 | Java | 🧩 Patches for ReVanced |

| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 5294 | Python | This repository is for active development of the Azure SDK for Python. For consumers of the SDK we recommend visiting our public developer docs at https://learn.microsoft.com/python/azure/ or our versioned developer docs at https://azure.github.io/azure-sdk-for-python. |

| [CodebuffAI/codebuff](https://github.com/CodebuffAI/codebuff) | 1456 | TypeScript | Generate code from the terminal! |

| [protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf) | 69053 | C++ | Protocol Buffers - Google's data interchange format |

| [facebook/folly](https://github.com/facebook/folly) | 29804 | C++ | An open-source C++ library developed and used at Facebook. |
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
