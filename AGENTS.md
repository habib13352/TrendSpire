# TrendSpire Agent Instructions

These guidelines apply to automation tools and human contributors.

## Key entry points
- `ai_loop/trendspire_autoloop.py` – main automation loop. Run with `python ai_loop/trendspire_autoloop.py --mode daily` or `--mode weekly`.
- `src/render_digest.py` – rebuilds `TRENDING.md` and injects it into the README.
- `src/api_logger.py` – records OpenAI API usage.
- `src/config.json` – central configuration for trending options.

## Directory overview
- `src/` – application modules.
- `ai_loop/` – automation scripts.
- `scripts/` – setup helpers (`setup_wizard.py`, `summarize_usage.py`).
- `tests/` – pytest suite.
- `TRENDING.md` & `README.md` – generated digest and documentation.
- `codex_logs/` & `trendspire_memory/` – automation output (do not commit).

## Conventions
1. Always run `pytest` before committing changes.
2. Use `python -m src.render_digest` when updating the trending digest.
3. Avoid committing files from `codex_logs/`, `trendspire_memory/` or `logs/`.
4. Pull request summaries should note which tests ran and highlight notable changes.
