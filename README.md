<!-- TRENDING_START -->
# 📈 GitHub Trending - Daily

_Last updated: 2025-06-06 06:49 UTC_

| Repository | ⭐ Stars | Language | Description |
|------------|--------:|----------|-------------|

| [frdel/agent-zero](https://github.com/frdel/agent-zero) | 8917 | Python | Agent Zero AI framework |

| [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | 7982 | Python | A high-performance algorithmic trading platform and event-driven backtester |

| [scrapy/scrapy](https://github.com/scrapy/scrapy) | 56218 | Python | Scrapy, a fast high-level web crawling & scraping framework for Python. |

| [onlook-dev/onlook](https://github.com/onlook-dev/onlook) | 16738 | TypeScript | The Cursor for Designers • An Open-Source Visual Vibecoding Editor • Visually build, style, and edit your React App with AI |

| [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) | 88045 | Dockerfile | 程序员在家做饭方法指南。Programmer's guide about how to cook at home (Simplified Chinese only). |

| [netbirdio/netbird](https://github.com/netbirdio/netbird) | 14181 | Go | Connect your devices into a secure WireGuard®-based overlay network with SSO, MFA and granular access controls. |

| [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | 4590 | Kotlin | 🪐 Markdown with superpowers — from ideas to presentations, articles and books. |

| [TapXWorld/ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook) | 36510 | Roff | 所有小初高、大学PDF教材。 |

| [ArduPilot/ardupilot](https://github.com/ArduPilot/ardupilot) | 12618 | C++ | ArduPlane, ArduCopter, ArduRover, ArduSub source |

| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 3025 | Python | Memory for AI Agents in 5 lines of code |
<!-- TRENDING_END -->

# TrendSpire

TrendSpire scrapes GitHub's trending page and generates a markdown digest of popular repositories. A GitHub Action keeps the `TRENDING.md` file updated on a daily schedule.

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
   An example configuration looks like:
   ```json
   {
     "language": "",
     "since": "daily",
     "limit": 10
   }
   ```
   After updating the configuration, run `python -m src.render_digest` again to regenerate `TRENDING.md`.

## GitHub Action

The workflow in `.github/workflows/update_digest.yml` regenerates the digest every day at 08:00 UTC and commits changes automatically.
