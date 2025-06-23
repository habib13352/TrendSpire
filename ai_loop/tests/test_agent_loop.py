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

