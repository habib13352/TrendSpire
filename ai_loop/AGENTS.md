# AI Agents Overview
This document outlines the automation agents used in TrendSpire.

## Directory Layout
- `src/`
  - Core scraper/render pipeline: `fetch_trending.py`, `render_digest.py`, `templates/trending.j2`, `config.json`
- `ai_loop/`
  - `autoloop.py` — CI and manual entry point
  - `agent_loop.py` — orchestrates the Planner → Coder → Reviewer → PR Agent pipeline
  - `agents/` — individual agent modules (`planner.py`, `coder.py`, `reviewer.py`, `pr_agent.py`)
  - `context_builder.py`, `suggestor.py`, `patcher.py`, `logger.py`, `improver.py` — modular components
  - `trendspire_memory/` — persistent context cache (future use)
  - `codex_logs/` — saved prompt/response logs
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
| **Planner** | internal call | ✅ Active | Read `GOALS.md` and produce a short plan |
| **Coder** | internal call | ✅ Active | Generate a patch diff from the plan and context |
| **Reviewer** | internal call | ✅ Active | LLM-powered review that approves or critiques diffs |
| **PR Agent** | internal call | ✅ Active | Format the diff into a pull request body |
| **autoloop** | workflow_dispatch, schedule | ✅ Active | Top-level entry that runs the pipeline |
| **codex_autobot** | manual dispatch | ✅ Active | One-off cleanup or file review |
| `trendspire_autoloop.py` | archived | 💤 Legacy | Old daily/weekly loop |
| `trendspire_codex_mixed.py` | archived | 💤 Legacy | Old per-file loop |

## Memory Usage
All agents receive a shared **context** dictionary from `context_builder.load_context()`.
This includes a short memory log from `trendspire_memory/memory.txt` when present.
- **Planner** reads the goals and memory excerpt to craft a high level plan.
- **Coder** uses the same context to generate a patch diff.
- **Reviewer** inspects the diff and returns approval status.
- **PR Agent** embeds the diff and may reference recent memory in the PR body.

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
Phase 2.3 added memory context and Phase 2.4 ensures graceful fallback if the
memory file is missing or the OpenAI call fails. Phase 2.5 introduced basic unit
tests for the agent loop and context builder. Phase 3 expands the agents with
safety checks and multiple planning options.
Phase 2 is now complete.

## Reviewer Logic
The Reviewer sends the proposed diff, project goals and repo summary to the OpenAI
Chat API using `call_openai_chat`. It returns an `approved` flag and free-form
comments. If the diff is empty or the API call fails, the pipeline defaults to
approval so execution never halts.
