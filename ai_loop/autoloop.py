"""Entry point for TrendSpire's AI loop."""

from .agent_loop import run as run_agent_loop


def main() -> None:
    """Execute the minimal agent pipeline."""
    pr_message = run_agent_loop()
    print(pr_message)


if __name__ == "__main__":
    main()
