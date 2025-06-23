"""Coding agent that turns a plan into a patch diff."""

from .. import suggestor


def _fallback_diff() -> str:
    return (
        "diff --git a/dummy.txt b/dummy.txt\n"
        "new file mode 100644\n"
        "index 0000000..e69de29\n"
        "--- /dev/null\n"
        "+++ b/dummy.txt\n"
        "@@\n"
        "+Placeholder content\n"
    )


def run(plan: list[str], context: dict | None = None) -> str:
    """Return a diff using `suggestor.suggest_patch` if possible."""
    print("[Coder] Received plan:", plan)
    if context is not None:
        try:
            diff = suggestor.suggest_patch(context)
            print("[Coder] Generated diff via suggestor")
            return diff
        except Exception as exc:  # pragma: no cover - network failure
            print("[Coder] Suggestor failed:", exc)

    diff = _fallback_diff()
    print("[Coder] Falling back to dummy diff")
    return diff
