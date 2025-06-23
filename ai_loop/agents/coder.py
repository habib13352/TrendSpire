"""Coding agent that turns a plan into a patch diff."""

from __future__ import annotations

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


def _diff_has_change(diff: str) -> bool:
    for line in diff.splitlines():
        if line.startswith("+++") or line.startswith("---"):
            continue
        if line.startswith("+") or line.startswith("-"):
            return True
    return False


def run(plan: list[list[str]] | list[str], context: dict | None = None) -> str:
    """Return a diff using `suggestor.suggest_patch` if possible."""
    print("[Coder] Received plan:", plan)
    if not plan:
        print("[Coder] Empty plan provided")
        return _fallback_diff()

    if isinstance(plan[0], list):
        chosen = plan[0]
    else:
        chosen = plan
    print("[Coder] Using plan steps:", chosen)

    if context is not None:
        try:
            diff = suggestor.suggest_patch(context)
            print("[Coder] Generated diff via suggestor")
            if _diff_has_change(diff):
                return diff
            print("[Coder] Diff lacked substantive changes")
        except Exception as exc:  # pragma: no cover - network failure
            print("[Coder] Suggestor failed:", exc)

    diff = _fallback_diff()
    print("[Coder] Falling back to dummy diff")
    return diff
