# TrendSpire Repository Overview

## Root
- **README.md** – project introduction and instructions.
- **TRENDING.md** – daily updated list of trending repositories.
- **main.py** – CLI entry point for the README improver tool.
- **dashboard.py** – small Streamlit dashboard showing last updates.

## `trendspire/`
- **fetch.py** – core trending scraper with `render_trending()` and helpers.
- **ai_patch.py** – OpenAI-powered README rewrite utilities.
- **ai_readme.py** – improves README content using trending data.
- **utils.py** – misc helpers: file IO, backups, logging and OpenAI helpers.
- **cli.py** – command line interface providing `fetch`, `ai-patch` and `ai-readme` subcommands.
- **templates/** – Jinja2 template for the trending digest.

## `ai_loop/`
- **trendspire_autoloop.py** – daily/weekly automation orchestrator.

## Other Folders
- **scripts/** – small helper scripts (setup wizard, usage summaries, etc.).
- **tests/** – pytest suite covering scraping, utilities and automation helpers.
- **codex_logs/** – stored diffs and logs from AI runs.
- **trendspire_memory/** – memory snapshots for Codex automation.
- **logs/** – API usage and update logs.
