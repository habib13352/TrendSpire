# TrendSpire

TrendSpire automatically fetches GitHub trending repositories and generates a markdown digest. A GitHub Action keeps the `TRENDING.md` file updated on a daily schedule.

## Getting Started

1. **Install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run locally**
   ```bash
   python -m src.render_digest
   ```
   The latest trending list will be written to `TRENDING.md`.

3. **Configuration**
   Edit `src/config.json` to set your preferred language, time range (`daily` or `weekly`), and number of repositories to include.

## GitHub Action

The workflow in `.github/workflows/update_digest.yml` regenerates the digest every day at 08:00 UTC and commits changes automatically.
