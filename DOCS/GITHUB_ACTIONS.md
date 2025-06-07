# GitHub Actions Overview

## update_digest.yml
This workflow runs every day at 08:00 UTC. It checks out the repository, installs Python dependencies and executes `python -m trendspire fetch`. That script scrapes GitHub Trending and generates `TRENDING.md`. Next it calls `python -m trendspire ai-readme` with `OPENAI_API_KEY` from secrets to polish the markdown. After running a small test it commits changes to `TRENDING.md`, `README.md` and API usage logs back to the `main` branch.

## auto_codex_mixed.yml
Triggered daily at 02:00 UTC, weekly at 03:00 UTC and on pushes or pull requests, this workflow installs dependencies and runs `ai_loop/trendspire_autoloop.py` with either `--mode daily` or `--mode weekly`. It uses both `OPENAI_API_KEY` and `GITHUB_TOKEN` secrets. The script fetches diffs, asks OpenAI for code suggestions, applies the patch, runs tests and pushes a new branch with a pull request. Logs and memory snapshots are uploaded as workflow artifacts and API usage is committed back to main.
