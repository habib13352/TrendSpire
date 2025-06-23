from ai_loop import sanity_checker


def test_sanity_all_good():
    diff = """diff --git a/x b/x
--- a/x
+++ b/x
@@
+hello
"""
    safe, reasons = sanity_checker.sanity_check_diff(diff)
    assert safe
    assert reasons == []


def test_sanity_flags_rm_rf():
    diff = """diff --git a/x b/x
--- a/x
+++ b/x
@@
+rm -rf /tmp
"""
    safe, reasons = sanity_checker.sanity_check_diff(diff)
    assert not safe
    assert any("rm -rf" in r for r in reasons)


def test_sanity_invalid_diff():
    safe, reasons = sanity_checker.sanity_check_diff("no diff here")
    assert not safe
    assert "Invalid" in reasons[0] or reasons
