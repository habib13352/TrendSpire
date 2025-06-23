# TrendSpire Phase 2 Report

This document summarizes the completion of **Phase 2** of the AI loop.
It reviews the new modules added, how agents interact, where logs and memory are stored, and what the GitHub Actions workflow now does.

## 2.1 – Agent Pipeline Scaffolding

Phase 2.1 introduced the high‑level agent modules and a minimal pipeline.
Key tasks from `GOALS.md` are listed below:

```text
- Added Planner, Coder, and PR Agent modules
- Wired pipeline via `agent_loop.py`
```

These tasks correspond to lines 62–64 in `GOALS.md`.

The new pipeline is orchestrated in `ai_loop/agent_loop.py`:

```python
print("[AgentLoop] Loading context")
context = context_builder.load_context()
print("[AgentLoop] Requesting patch suggestion")
diff = suggestor.suggest_patch(context)
print("[AgentLoop] Formatting PR")
pr_message = pr_agent.format_pr(diff)
print("[AgentLoop] Pipeline complete")
```

## 2.2 – Real Context and Suggestion

Phase 2.2 connected the pipeline to real data:

- **Context Builder** reads the README, `GOALS.md`, a summary of `src/`, the latest trend snapshot, and `TRENDING.md`.
- **Suggestor** crafts an OpenAI prompt, sends the request, and logs the token usage and cost via `logger.py`.
- **PR Agent** formats the diff into a simple PR body.

Running `agent_loop.py` now prints `"✅ Phase 2.2 complete: AI suggestion generated."`

## Agent Behavior Changes

The AI loop now performs the following steps when executed:

1. **Load context** from the repository and trend archives.
2. **Send a prompt** to OpenAI requesting a patch.
3. **Log** the prompt, response, token counts, and estimated cost to `ai_loop/codex_logs/`.
4. **Format** the diff into a PR message (patch application is still a TODO in `patcher.py`).

The planner and coder modules exist but currently return placeholder data.

## Memory and Log Artifacts

Artifacts produced by the AI loop are stored under `ai_loop/`:

| Path | Purpose |
|------|---------|
| `codex_logs/` | Per-run prompt/response logs |
| `codex_costs.csv` | Aggregate usage costs |
| `trendspire_memory/` | Cached state between runs |
| `metrics/ci_runs.csv` | CI job exit codes |

Example log listing:

```bash
$ ls ai_loop/codex_logs
file
log_20250623-185454.txt
```

## GitHub Action Behavior

The workflow `.github/workflows/ai_loop.yml` now performs several steps:

1. Restore cached memory and build repository context.
2. Upload log artifacts if found.
3. Run `python -m ai_loop.autoloop` on daily or weekly triggers.
4. Always upload `codex_logs` and `trendspire_memory` artifacts.
5. Commit API usage logs back to `main`.

Relevant excerpt from the workflow:

```yaml
- name: Check Codex Logs
  id: context_logs
  run: |
    if [ -d ai_loop/codex_logs ]; then
      echo "found=true" >> "$GITHUB_OUTPUT"
    else
      echo "::warning::ai_loop/codex_logs not found" >&2
      echo "found=false" >> "$GITHUB_OUTPUT"
    fi
- name: Upload Codex Logs
  if: steps.context_logs.outputs.found == 'true'
  uses: actions/upload-artifact@v4
  with:
    name: codex-logs
    path: ai_loop/codex_logs/
```

## Optional Cleanup

No additional cleanup was required in this phase beyond the refactors completed during Phase 1.5. Legacy scripts remain archived under `ai_loop/legacy/` for reference.

## Final Verdict & Phase 3 Preview

All Phase 2 tasks are complete and unit tests pass. The AI loop can load context, call OpenAI, log results, and produce a PR message. Patch application remains stubbed for Phase 3.

Phase 3 will introduce multi-step reasoning and role-based agents (Planner → Coder → Reviewer) as outlined in `GOALS.md`. The AI loop can be invoked in the future with:

```bash
python -m ai_loop.autoloop
```

**Status:** Ready to begin Phase 3.
