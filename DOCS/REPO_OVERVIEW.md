# TrendSpire Repository Overview

## Root
- **README.md** – project introduction and instructions.
- **TRENDING.md** – daily updated list of trending repositories.
- **main.py** – CLI entry point for the README improver tool.
- **dashboard.py** – small Streamlit dashboard showing last updates.
- **monitor_status.py** – checks automation health and posts alerts.
- **post_comment.py** – posts suggestions.md as a PR comment via `gh`.
- **sanity_check.py** – quick checks ensuring expected files exist.

## `src/`
- **fetch_trending.py** – `fetch_trending()` scrapes GitHub Trending and returns a list of repos. Includes helpers `render_markdown()` and `save_trending()`.
- **render_digest.py** – `render_trending()` writes `TRENDING.md` using a Jinja template and calls `fetch_trending`.
- **improve_markdown.py** – cleans and rewrites markdown files with OpenAI.
- **api_logger.py** – `log_openai_usage()` records API usage in csv/json/txt.
- **openai_helper.py** – `ask_openai()` thin wrapper around the OpenAI chat API.
- **openai_call.py** – one-off helper `improve_trending_md()` used by scripts.
- **check_ai_quality.py** – validates README structure and posts an issue if sections are missing.
- **readme_loader.py** – simple `load_readme()` utility.
- **utils.py** – misc helpers: file IO, backups, logging, `openai_chat()`, and `fetch_url()`.
- **logger.py** – exports `get_trendspire_logger(name)` for unified logging.
- **templates/** – Jinja2 template for trending digest.

## `ai_loop/`
- **ai_readme.py** – improves README content using trending data.
- **codex_autobot.py** – per-file Codex analysis and PR creation.
- **improver.py** – OpenAI-powered README rewrite utilities.
- **trendspire_autoloop.py** – daily/weekly automation orchestrator.
- **trendspire_codex_mixed.py** – alternate AI workflow combining diff and file review.

## Other Folders
- **scripts/** – small helper scripts (setup wizard, usage summaries, etc.).
- **tests/** – pytest suite covering scraping, utilities and automation helpers.
- **codex_logs/** – stored diffs and logs from AI runs.
- **trendspire_memory/** – memory snapshots for Codex automation.
- **logs/** – API usage and update logs.
