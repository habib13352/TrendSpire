"""Run README improvement using OpenAI."""

from trendspire.ai_readme import improve_readme
from src.agents_logger import log_agent_action


def main() -> None:
    changed = improve_readme(enable=True)
    if changed:
        log_agent_action("ReadmeUpdaterAgent", "README improved via OpenAI")
    else:
        log_agent_action("ReadmeUpdaterAgent", "README unchanged")


if __name__ == "__main__":
    main()
