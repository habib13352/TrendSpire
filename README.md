<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-08-02 12:28 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [dyad-sh/dyad](https://github.com/dyad-sh/dyad) | 3390 | TypeScript | Free, local, open-source AI app builder | v0 / lovable / Bolt alternative | 🌟 Star if you like it! |

| [pointfreeco/swift-composable-architecture](https://github.com/pointfreeco/swift-composable-architecture) | 13598 | Swift | A library for building applications in a consistent and understandable way, with composition, testing, and ergonomics in mind. |

| [MotiaDev/motia](https://github.com/MotiaDev/motia) | 4468 | TypeScript | Unified Backend Framework for APIs, Events, and AI Agents |

| [OpenBAS-Platform/openbas](https://github.com/OpenBAS-Platform/openbas) | 1196 | Java | Open Adversary Exposure Validation Platform |

| [tonsky/FiraCode](https://github.com/tonsky/FiraCode) | 79591 | Clojure | Free monospaced font with programming ligatures |

| [kubesphere/kubesphere](https://github.com/kubesphere/kubesphere) | 16377 | Go | The container platform tailored for Kubernetes multi-cloud, datacenter, and edge management ⎈ 🖥 ☁️ |

| [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) | 192485 | JavaScript | 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings |

| [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) | 157386 | Unknown | Master the command line, in one page |

| [lydiahallie/javascript-questions](https://github.com/lydiahallie/javascript-questions) | 64357 | Unknown | A long list of (advanced) JavaScript questions, and their explanations ✨ |

| [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | 180562 | Unknown | A collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools and more. |
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
