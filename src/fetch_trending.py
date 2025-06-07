"""Script entry point for the TrendingFetcherAgent."""

from trendspire.fetch import render_trending, update_readme
from src.agents_logger import log_agent_action


def main() -> None:
    markdown = render_trending()
    update_readme(markdown)
    log_agent_action("TrendingFetcherAgent", "Fetched trending repositories")


if __name__ == "__main__":
    main()
