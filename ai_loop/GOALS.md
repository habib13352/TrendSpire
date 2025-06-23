# AI Loop Roadmap

This document tracks development milestones for TrendSpire's autonomous improvement loop. The phases mirror the repository's global roadmap but focus on the `ai_loop/` subsystem.

## ✅ Phase 1.5 – Cleanup & Scaffolding
- Archived legacy automation scripts.
- Created modular components: `context_builder.py`, `suggestor.py`, `patcher.py`, and `logger.py`.
- Established `autoloop.py` as the entry point for local runs and CI.

## 🚀 Phase 2 – Context‑Aware Agent Loop
AI agents ingest repository context and generate patch suggestions.

### ✅ Phase 2.1 – Agent Pipeline Scaffolding
- Introduced minimal agents: **Planner**, **Coder**, and **PR Agent**.
- Wired them together in `agent_loop.py`.

### ✅ Phase 2.2 – First End‑to‑End Run
- `context_builder.load_context()` supplies README, goals and trend summaries.
- `suggestor.suggest_patch()` sends this context to OpenAI and returns a diff.
- `pr_agent.format_pr()` converts the diff into a pull request body.

The result is a working pipeline that prints a PR message but does not yet apply patches.

## ✅ Phase 2.3 – Enhanced Context Usage
Agents now load an optional memory excerpt from `trendspire_memory/memory.txt`.
`agent_loop.run()` passes this context through Planner and Coder so the diff
can reference recent activity.

## ✅ Phase 2.4 – Memory Fallback Handling
`context_builder.load_context()` now returns an empty string when the memory
log is absent. `coder.run()` also falls back to a dummy diff if the OpenAI
request fails.

## ✅ Phase 2.5 – Validation Tests
Unit tests now cover `agent_loop.run()` and `context_builder.load_context()` to
ensure memory is included when available and ignored when missing.

Future phases (3‑5) will expand multi‑step reasoning, trend analysis and automated pull requests.
