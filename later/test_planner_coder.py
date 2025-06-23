from ai_loop.agents import planner, coder


def test_planner_multiple_plans():
    ctx = {"src_summary": "a.py, b.py"}
    plans = planner.run(ctx)
    assert isinstance(plans, list)
    assert len(plans) >= 2
    assert all(isinstance(p, list) for p in plans)


def test_coder_rejects_empty_diff(monkeypatch):
    plan = [["step"]]
    monkeypatch.setattr("ai_loop.suggestor.suggest_patch", lambda ctx: "diff --git a/x b/x\n")
    diff = coder.run(plan, {})
    assert "+Placeholder content" in diff
