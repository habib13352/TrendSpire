<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-06-10 12:29 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [jwohlwend/boltz](https://github.com/jwohlwend/boltz) | 2201 | Python | Official repository for the Boltz biomolecular interaction models |

| [tensorzero/tensorzero](https://github.com/tensorzero/tensorzero) | 6137 | Rust | TensorZero creates a feedback loop for optimizing LLM applications — turning production data into smarter, faster, and cheaper models. |

| [alphacep/vosk-api](https://github.com/alphacep/vosk-api) | 11275 | Jupyter Notebook | Offline speech recognition API for Android, iOS, Raspberry Pi and servers with Python, Java, C# and Node |

| [friuns2/BlackFriday-GPTs-Prompts](https://github.com/friuns2/BlackFriday-GPTs-Prompts) | 7510 | Unknown | List of free GPTs that doesn't require plus subscription |

| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 57442 | MDX | 🐙 Guides, papers, lecture, notebooks and resources for prompt engineering |

| [eythaann/Seelen-UI](https://github.com/eythaann/Seelen-UI) | 7851 | Rust | The Fully Customizable Desktop Environment for Windows 10/11. |

| [ourongxing/newsnow](https://github.com/ourongxing/newsnow) | 10751 | TypeScript | Elegant reading of real-time and hottest news |

| [zijie0/HumanSystemOptimization](https://github.com/zijie0/HumanSystemOptimization) | 16521 | Unknown | 健康学习到150岁 - 人体系统调优不完全指南 |

| [datawhalechina/self-llm](https://github.com/datawhalechina/self-llm) | 16731 | Jupyter Notebook | 《开源大模型食用指南》针对中国宝宝量身打造的基于Linux环境快速微调（全参数/Lora）、部署国内外开源大模型（LLM）/多模态大模型（MLLM）教程 |

| [XTLS/Xray-core](https://github.com/XTLS/Xray-core) | 29125 | Go | Xray, Penetrates Everything. Also the best v2ray-core. Where the magic happens. An open platform for various uses. |
<!-- TRENDING_END -->

# TrendSpire

TrendSpire gathers trending repositories from GitHub and stores them in `TRENDING.md`. GitHub Actions keep the digest fresh and leverage OpenAI Codex to continuously improve the codebase.

## Features

- Automated scraping of GitHub's trending page with configurable language, time range and result limit.
- Daily workflow to regenerate `TRENDING.md` and update this README.
- Scheduled Codex runs that suggest small refactors and new tests via pull requests.
- Token and cost tracking for all Codex requests.
- Persistent memory stored under `trendspire_memory/` enables the AI to
  iteratively refine its suggestions across runs and open automated pull
  requests with context.

## What TrendSpire Does Today

- `python -m src.fetch_trending` — scrape GitHub Trending
- `python -m src.render_digest` — render TRENDING.md & inject into README.md

### AI Agents (coming soon)
See [AGENTS.md](./AGENTS.md) and [ai_loop/README.md](./ai_loop/README.md) for details on the self-improvement loop.

## Getting Started

1. **Install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the setup wizard**
   ```bash
   python scripts/setup_wizard.py
   ```
   This interactive script stores your preferred trending options and OpenAI API key.
   You can rerun it at any time to change the configuration.

3. **Run the trending scraper**
   ```bash
   python -m src.render_digest
   ```
   The latest results will appear in `TRENDING.md` and the README.


## GitHub Actions

### Update Digest

The workflow [`update_digest.yml`](.github/workflows/update_digest.yml) runs every day at 08:00 UTC. It installs the dependencies, executes `python -m src.render_digest`, and commits any changes to `TRENDING.md` and `README.md`.

### Codex Automation

Another workflow [`ai_loop.yml`](.github/workflows/ai_loop.yml) drives the Codex automation using [`ai_loop/trendspire_autoloop.py`](ai_loop/trendspire_autoloop.py). It supports two modes:

- **Daily** – diff-based improvements using `gpt-3.5-turbo`.
- **Weekly** – a full repository review with `gpt-4o`.

Each run applies the returned diff, executes the test suite and, when successful, creates a branch and pull request. Summaries, cost logs and the raw diff are saved under `codex_logs/` and uploaded as workflow artifacts. The workflow also caches the `trendspire_memory/` directory so the AI can refine its suggestions over time.

To run the Codex automation locally you can execute:

```bash
python ai_loop/trendspire_autoloop.py --mode daily   # or weekly
```

### API usage reports

The file `logs/api_usage.*` records token counts and cost. Set `API_LOG_FORMAT`
to `csv`, `json` or `txt` to control the format. Run `python
scripts/summarize_usage.py` for a quick summary grouped by model.

### Running tests

After installing the requirements you can run the entire test suite with

```bash
pytest
```

Additional tips for contributors are available in
[docs/DEVELOPER.md](docs/DEVELOPER.md).
