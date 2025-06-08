# AI Agents Overview
This document outlines the automation agents used in TrendSpire.

## Directory Layout
- `src/`
  - Core scraper/render pipeline: `fetch_trending.py`, `render_digest.py`, `templates/trending.j2`, `config.json`
- `ai_loop/`
  - `trendspire_autoloop.py` — daily/weekly patch-based loop
  - `trendspire_codex_mixed.py` — per-file improvement loop
  - `codex_autobot.py` — standalone file-by-file review tool
  - `api_logger.py` — logs token & cost usage
  - `scripts/` — helper scripts (setup, summarization)
  - `tests/` — unit tests for AI agents
  - `.github/workflows/ai_loop.yml` — CI triggers for AI-loop
- Root files:
  `README.md`, `TRENDING.md`, `requirements.txt`, `.env.example`, `docs/DEVELOPER.md`
- Root CI:
  `.github/workflows/update_digest.yml`

## Agent Responsibilities
| Agent | Trigger | Purpose |
|-------|---------|---------|
| autoloop (daily) | schedule: daily | Apply small diffs and open PRs automatically |
| autoloop (weekly) | schedule: weekly | Deep refactor & audit, store summaries |
| mixed (per-file loop) | manual dispatch | Review each file, generate PR per file |
| codex_autobot | manual dispatch | One-off cleanup or targeted improvements |

## How to Run
```bash
# Core:
python -m src.fetch_trending
python -m src.render_digest

# AI Loop:
python ai_loop/trendspire_autoloop.py --mode daily
python ai_loop/trendspire_autoloop.py --mode weekly
python ai_loop/trendspire_codex_mixed.py --mode mixed
python ai_loop/codex_autobot.py
```

## Configuration & Secrets
- `.env` variables: `OPENAI_API_KEY`
- Core config: `config.json`
- `ai_loop` env: optional `API_LOG_FORMAT` for log output
- Additional YAML configs under `ai_loop/` (`auto_codex_mixed.yml`, `autobot.yml`)

## CI Workflow Mapping
- Core digest: `.github/workflows/update_digest.yml`
- **AI agents**: ai_loop/.github/workflows/ai_loop.yml (runs on ai_loop/**)

## Prompt Templates
- Trending digest template: `src/templates/trending.j2`
- AI-loop templates:
  - `ai_loop/prompts/autobot.j2`
  - `ai_loop/prompts/daily.diff.j2`
  - `ai_loop/prompts/per_file.j2`
  - `ai_loop/prompts/weekly.refactor.j2`

## Next Steps
- Keep this file updated as you add or modify agents
- Version your prompt templates
- Centralize shared helpers
- Shared helpers, prompt templates, rollback logic, metrics and docs are now in place
