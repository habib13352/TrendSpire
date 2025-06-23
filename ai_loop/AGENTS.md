# AI Agents Overview
This document outlines the automation agents used in TrendSpire.

## Directory Layout
- `src/`
  - Core scraper/render pipeline: `fetch_trending.py`, `render_digest.py`, `templates/trending.j2`, `config.json`
- `ai_loop/`
  - `autoloop.py` — Phase 1.5 entrypoint for the AI workflow
  - `context_builder.py`, `suggestor.py`, `patcher.py`, `logger.py`, `improver.py` — modular components
  - `legacy/` — archived scripts (`trendspire_autoloop.py`, `trendspire_codex_mixed.py`)
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
| Agent | Trigger | Status | Purpose |
|-------|---------|--------|---------|
| autoloop | workflow_dispatch, schedule | ✅ Active | Main entrypoint, runs placeholder logic (Phase 1.5) |
| codex_autobot | Manual dispatch | ✅ Active | One-off cleanup or file review |
| trendspire_autoloop.py | Archived | 💤 Legacy | Old daily/weekly loop, moved to legacy/ |
| trendspire_codex_mixed.py | Archived | 💤 Legacy | Old per-file loop, moved to legacy/ |

## How to Run
```bash
# Core:
python -m src.fetch_trending
python -m src.render_digest

# AI Loop:
python -m ai_loop.autoloop
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
Phase 2 will connect `context_builder.py`, `suggestor.py`, and `patcher.py`.
The AI agent will begin analyzing repo structure and propose changes based on
GitIngest and trending data. Logs and memory will be saved to support
iterative suggestions.
