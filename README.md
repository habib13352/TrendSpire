![Logo](assets/logo.png)

# 🚀 TrendSpire

Welcome to **TrendSpire**! This project is your gateway to effortlessly staying informed about the most popular repositories on GitHub. 🕵️‍♂️ It automatically gathers and updates a list of trending repositories, keeping developers and content creators in the loop with the latest open-source contributions.

## 📌 Project Purpose

The primary goal of TrendSpire is to automate the collection of trending GitHub repositories and maintain an up-to-date digest in `TRENDING.md`. By harnessing the power of GitHub Actions and OpenAI Codex, TrendSpire continuously improves itself — making it a smart choice for tech enthusiasts who wish to stay updated with minimal effort.

## ✨ Features

- 🔄 **Automated Scraping**: Configurable scraping of GitHub's trending page by language, time range, and result limit.
- 📅 **Daily Updates**: Scheduled workflows regenerate `TRENDING.md` daily and refresh this README.
- 🤖 **Codex-Aided Improvements**: Regular AI-driven refactoring and test additions via pull requests.
- 💰 **Cost Tracking**: Logs and monitors token usage and costs for all Codex requests.
- 🧠 **Persistent Memory**: Stores iterative improvements under `trendspire_memory/`, enhancing AI suggestion accuracy and context.

## Trending This Week
<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-06-07 02:48 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [netbirdio/netbird](https://github.com/netbirdio/netbird) | 14709 | Go | Connect your devices into a secure WireGuard®-based overlay network with SSO, MFA and granular access controls. |

| [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) | 5317 | Python | Build effective agents using Model Context Protocol and simple workflow patterns |

| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 3391 | Python | Memory for AI Agents in 5 lines of code |

| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | 24892 | Python | DSPy: The framework for programming—not prompting—language models |

| [codexu/note-gen](https://github.com/codexu/note-gen) | 3334 | TypeScript | A cross-platform Markdown note-taking application dedicated to using AI to bridge recording and writing, organizing fragmented knowledge into a readable note. |

| [unslothai/notebooks](https://github.com/unslothai/notebooks) | 1338 | Jupyter Notebook | Fine-tune LLMs for free with guided Notebooks on Google Colab, Kaggle, and more. |

| [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | 319288 | Unknown | A complete computer science study plan to become a software engineer. |

| [deepsense-ai/ragbits](https://github.com/deepsense-ai/ragbits) | 884 | Python | Building blocks for rapid development of GenAI applications |

| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 90004 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |

| [coleam00/Archon](https://github.com/coleam00/Archon) | 4722 | Python | Archon is an AI agent that is able to create other AI agents using an advanced agentic coding workflow and framework knowledge base to unlock a new frontier of automated agents. |
<!-- TRENDING_END -->

## 🔍 How it Works

TrendSpire utilizes GitHub Actions to automate daily updates and deploys OpenAI Codex to implement suggestions for code improvements. It uses scheduled tasks to scrape trending data, applies updates, and generates pull requests using intelligent code analysis and improvements.

## 🚀 Getting Started

Follow these steps to set up and run TrendSpire:

1. **Install Dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the Setup Wizard**
   ```bash
   python scripts/setup_wizard.py
   ```
   Save your OpenAI API key to `.env` and optional preferences to `config.yaml`. Rerun any time to update your settings.

3. **Execute the Trending Scraper**
   ```bash
   python -m trendspire fetch
   ```
   View the latest trends in the `TRENDING.md` file and this README.

4. **Activate the Self-Improvement Loop**
   ```bash
   python trendspire_autoloop.py --mode daily
   ```
   Switch to `weekly` for a comprehensive review. Tracks diff history and applies changes.

5. **Enable PR Workflows**
   Activate GitHub Actions on your fork for automatic pull requests.

## 🤝 Contributing

We welcome contributions! Check out [docs/DEVELOPER.md](docs/DEVELOPER.md) for guidelines. Feel free to open issues or pull requests for suggestions, improvements, or bug fixes.

## Acknowledgements
Thanks to OpenAI and the community for feedback.

## Maintainers
- Alice Johnson (@alicej)
- Bob Smith (@bobsmith)

## 📜 License

TrendSpire is licensed under the [MIT License](LICENSE). Feel free to use, distribute, and modify it within the terms of the license.

## 💡 Want to Learn More?

### GitHub Actions

**Update Digest**: Runs daily at 08:00 UTC to update trending data and README.

**Codex Automation**: Uses `trendspire_autoloop.py` for daily or weekly improvements and PR creation. Caches memory for smarter AI over time.

### API Usage Reports

Logs are stored in `logs/api_usage.*`. Customize log format via `API_LOG_FORMAT`.

### Running Tests

Execute the entire test suite with:

```bash
pytest
```

## Contact
- Email: you@example.com

Thank you for checking out TrendSpire! Stay trendy and happy coding! 👩‍💻👨‍💻