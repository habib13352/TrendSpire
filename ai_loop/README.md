# AI Loop Guide

TrendSpire's AI loop automates small code improvements using OpenAI. It loads repository context, asks the models for a diff and prints a pull request body. Runs happen both locally and in GitHub Actions.

## Local usage

Build the repository context and run the minimal pipeline:

```bash
python -m ai_loop.context_builder   # updates trendspire_memory/memory.txt
python -m ai_loop.agent_loop        # prints a PR message
```

`autoloop.py` wraps the same call and is used by CI:

```bash
python -m ai_loop.autoloop
```

For targeted cleanups you can run the autobot:

```bash
python ai_loop/codex_autobot.py
```

## Testing modules

Unit tests live under `ai_loop/tests/`. Execute a single module's tests with:

```bash
pytest ai_loop/tests/test_context_builder.py
pytest ai_loop/tests/test_agent_loop.py
pytest ai_loop/tests/test_api_logger.py
```

Add more tests as modules like `patcher.py` evolve. The full suite runs with:

```bash
pytest
```

## Checking logs and memory

- OpenAI call logs appear in `ai_loop/codex_logs/` as `log_<timestamp>.txt`.
- Cumulative cost data is stored in `ai_loop/codex_costs.csv`.
- The context builder appends to `ai_loop/trendspire_memory/memory.txt`.

Use `ls ai_loop/codex_logs` or `tail -n 5 ai_loop/trendspire_memory/memory.txt` to confirm new entries after a run.

## GitHub Action workflow

The workflow [.github/workflows/ai_loop.yml](../.github/workflows/ai_loop.yml) triggers on pushes to `ai_loop/**` or by manual dispatch. Key steps:

1. Checkout the repo and install dependencies.
2. Restore cached `trendspire_memory/`.
3. Run `python -m ai_loop.context_builder` to refresh memory.
4. Execute `python -m ai_loop.autoloop` (daily or weekly mode).
5. Upload `ai_loop/codex_logs/` and `ai_loop/trendspire_memory/` as artifacts.
6. Commit API usage logs back to the repository.

## CI artifacts

Workflow runs expose these downloadable artifacts:

- **codex-logs** / **codex-logs-final** – raw OpenAI prompts and responses.
- **codex-memory** – the updated `trendspire_memory/` directory.

Inspect them to see exactly what the agents produced during CI.

## Prompt templates

Agent prompts live in `ai_loop/prompts/`:

- `autobot.j2`
- `daily.diff.j2`
- `per_file.j2`
- `weekly.refactor.j2`

