"""Placeholder coding agent."""


def run(plan: list[str]) -> str:
    """Return a dummy diff string for the given plan."""
    print("[Coder] Received plan:", plan)
    diff = """diff --git a/dummy.txt b/dummy.txt
new file mode 100644
index 0000000..e69de29
--- /dev/null
+++ b/dummy.txt
@@
+Placeholder content
"""
    print("[Coder] Generated dummy diff")
    return diff
