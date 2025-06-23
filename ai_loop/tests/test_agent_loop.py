import importlib
from pathlib import Path

import ai_loop.agent_loop as agent_loop


def test_agent_loop_passes_context(monkeypatch):
    fake_context = {"readme": "r", "goals": "g", "memory": "m"}
    monkeypatch.setattr(agent_loop.context_builder, "load_context", lambda: fake_context)

    captured = {}

    def fake_suggest(ctx):
        captured["ctx"] = ctx
        return "diff --git a/x b/x\n+test"

    monkeypatch.setattr("ai_loop.suggestor.suggest_patch", fake_suggest)

    msg = agent_loop.run()
    assert captured["ctx"] == fake_context
    assert "diff --git" in msg


def test_agent_loop_returns_failure_message(monkeypatch):
    monkeypatch.setattr(agent_loop.context_builder, "load_context", lambda: {})
    monkeypatch.setattr(agent_loop, "run_planner", lambda ctx: ["plan"])
    monkeypatch.setattr(agent_loop, "run_coder", lambda plan, ctx: "bad diff")
    monkeypatch.setattr(agent_loop, "review_patch", lambda diff, ctx: {"approved": True, "comments": ""})
    monkeypatch.setattr(agent_loop, "sanity_check_diff", lambda d: (False, ["boom"]))

    msg = agent_loop.run()
    assert msg.startswith("Sanity check failed")

