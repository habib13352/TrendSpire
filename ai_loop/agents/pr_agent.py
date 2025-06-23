"""Pull request formatting agent."""


def format_pr(diff: str) -> str:
    """Return a simple PR body for the given diff."""
    pr_body = (
        "### Proposed Changes\n\n"
        f"```diff\n{diff}\n```\n"
    )
    return pr_body


def run(diff: str) -> str:  # pragma: no cover - legacy alias
    print("[PR Agent] Formatting PR message")
    return format_pr(diff)
