# Developer Guide

This guide walks through the main steps for setting up a local environment and contributing to TrendSpire.

## Setting up your environment

TrendSpire requires Python 3.10 or newer. Create a virtual environment and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Next run the interactive setup wizard. It stores your OpenAI API key in `.env` and saves preferences in `config.yaml`:

```bash
python scripts/setup_wizard.py
```

## Running the test suite

With the virtual environment active you can execute all tests using `pytest`:

```bash
pytest
```

Pytest is listed in `requirements.txt` so it will be installed automatically.

## Customising the trending configuration

The scraper configuration lives in [`config.yaml`](../config.yaml). You can edit this file directly or rerun the setup wizard if you want to change the language, time range or result limit.

After updating the config regenerate the digest with:

```bash
python -m trendspire fetch
```

This refreshes `TRENDING.md` and injects the table into the README between the `<!-- TRENDING_START -->` and `<!-- TRENDING_END -->` markers.

## API usage logs

OpenAI API usage is recorded under the `logs/` directory. Set the `API_LOG_FORMAT` environment variable to `csv`, `json` or `txt` to control the output format.

## Codex automation

The script `trendspire_autoloop.py` runs the self-improvement loop. Invoke it with `--mode daily` or `--mode weekly` to let the AI propose improvements. The script stores diff history in `trendspire_memory/`, applies the changes and runs the tests before opening a pull request.



