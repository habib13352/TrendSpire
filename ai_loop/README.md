# AI-loop Subsystem

TrendSpire's **AI-loop** automates code improvements using OpenAI models. It runs in several modes and integrates with GitHub Actions to open pull requests after successful tests.

## Running the loops

Daily and weekly modes are now handled by `autoloop.py`:

```bash
python -m ai_loop.autoloop
```

Older scripts have been moved under `ai_loop/legacy/` for reference.

The `codex_autobot.py` script performs targeted cleanups:

```bash
python ai_loop/codex_autobot.py
```

## Prompt templates

Templates for the agents live under `ai_loop/prompts/`:

- `autobot.j2`
- `daily.diff.j2`
- `per_file.j2`
- `weekly.refactor.j2`

## Running tests and CI locally

Unit tests reside in `ai_loop/tests/` and can be executed with:

```bash
pytest ai_loop/tests
```

The GitHub Actions workflow `ai_loop/.github/workflows/ai_loop.yml` mirrors these steps. Install the requirements and run the commands above to reproduce the CI jobs locally.


