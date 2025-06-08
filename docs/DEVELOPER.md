# Developer Guide

This short guide covers common tasks for working on TrendSpire.

## Running the test suite
Run all tests with:

```bash
pytest
```

Pytest is listed in `requirements.txt` so it will be installed with the other dependencies.

## Customising the trending configuration
The scraper configuration lives in [`src/config.json`](../src/config.json). You can edit this file directly or run the interactive setup wizard:

```bash
python scripts/setup_wizard.py
```

The wizard also stores your `OPENAI_API_KEY` in `.env`.

After updating the config you can regenerate the digest with:

```bash
python -m src.render_digest
```

This will refresh `TRENDING.md` and inject the table into the README between the
`<!-- TRENDING_START -->` and `<!-- TRENDING_END -->` markers.

## Codex automation
The automated self-improvement tools live in `ai_loop/`. Run the loop manually with:
```bash
python ai_loop/trendspire_autoloop.py --mode daily   # or weekly
```
The workflow `.github/workflows/ai_loop.yml` schedules runs on GitHub.
