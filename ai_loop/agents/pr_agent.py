"""Placeholder PR formatting agent."""


def run(diff: str) -> str:
    """Return a dummy PR body for the given diff."""
    print("[PR Agent] Formatting PR message")
    pr_body = (
        "### Proposed Changes\n\n"
        "This PR includes the following dummy diff:\n\n"
        f"```diff\n{diff}\n```"
    )
    return pr_body
