# 🧠 TrendSpire – Project Goals & Roadmap

TrendSpire is a self-improving, trend-aware GitHub repository that automatically:
- Tracks trending GitHub repos and saves snapshots
- Analyzes repo structure, docs, and tech patterns
- Suggests improvements via AI
- Opens pull requests with patches
- Evolves based on open-source trends

---

## 🎯 Core Vision

Build a fully automated developer assistant that:
- **Monitors the repo and tech ecosystem**
- **Suggests and applies useful changes**
- **Opens PRs for human review**
- **Learns from trend data over time**

---

## 🧱 PHASED ROADMAP

### ✅ Phase 1 – Trending Digest + Archival (Complete)
- Automate fetching trending GitHub repositories daily
- Save snapshots as both `.md` and `.json` files
- Store all historical snapshots in `trends/archive/`
- Update root `TRENDING.md` and `README.md` with latest trend

---

### 🔧 Phase 1.5 – Codebase Cleanup (Now)
**Goal:** Refactor `ai_loop/` to be lean and modular for AI integration

Tasks:
 - ✅ Delete or archive unused scripts (`trendspire_autoloop.py`, etc.)
 - ✅ Simplify `improver.py` to keep only working patch/prompt logic
 - ✅ Create scaffolding modules:
  - `context_builder.py`
  - `suggestor.py`
 - `logger.py`
 - Archived unused helpers `patcher.py` and `improver.py`
 - ✅ Setup `autoloop.py` as single entrypoint: `python -m ai_loop.autoloop`
 - ✅ Confirm trending/archival system still runs cleanly

---

### ✅ Phase 2 – AI Suggestion Loop (Complete)
**Goal:** AI reads your repo + recent trends and suggests useful patches**

Modules:
- `context_builder.py` → Loads README, key files, trend snapshot
- `suggestor.py` → Crafts OpenAI prompt and parses response
- `logger.py` → Tracks tokens, cost, and output for traceability

Features:
- Runs manually or on schedule
- Logs each AI action and cost
- Stores patches in versioned branches

### ✅ Phase 2.1 – Agent Pipeline Scaffolding (Complete)
- Added Planner, Coder, and PR Agent modules
- Wired pipeline via `agent_loop.py`

### ✅ Phase 2.2 – Memory & Logging (Complete)
- Context builder reads README, goals and latest trends
- Pipeline passes a short memory excerpt between agents
- Logs and memory artifacts uploaded via CI


---

### 🧠 Phase 3 – Agentic Workflow
**Goal:** Enable multi-step reasoning and iteration

Upgrades:
- Allow multi-turn conversations per suggestion
- Implement roles: Planner → Coder → Reviewer
- Integrate feedback loops if patch breaks tests

### ✅ Phase 3.1 – Reviewer Agent (Complete)
- Added an LLM-powered Reviewer that critiques the diff
- Each agent step logs output in `ai_loop/codex_logs/`
- Reviewer comments appear in the PR body

### ✅ Phase 3.2 – Sanity Checker Agent (Complete)
- Validate diffs before PR creation and flag obvious issues

---

### 📊 Phase 4 – Trend-Aware Reasoning
**Goal:** Let AI learn from past trend archives to guide decisions

Tasks:
- Parse and embed `.json` snapshots
- Detect pattern changes across time
- AI says: _“X is trending — adapt your repo to match”_

✅ Phase 4 Kickoff Checklist — Trend-Aware Reasoning
🎯 Goal
Learn from trends/archive/*.json over time and use that knowledge to guide smarter planning.

🔧 Development Tasks
1. Parse & Summarize Archived Trends
 In context_builder.load_context(), read all or recent .json files from trends/archive/

 Generate a summary (e.g. frequency of languages, common repo names/tags)

 Add this summary as context["trend_summary"]

2. Use Trend Summary in Planning
 In run_planner(), allow planner agents to use trend_summary for:

Detecting repeated repos

Spotting fast-growing projects

Choosing which type of improvements to recommend

 You can even add a trend_strategy_agent.py module if helpful

3. Test It
 Write unit tests that simulate archived trends

 Test expected plan behaviors (e.g., it should avoid duplicate repos or favor newer rising stars)

🧼 Optional Cleanup (Strongly Recommended)
 ✅ Update AGENTS.md → Document what Phase 3 completed (context, memory, sanity check, etc.)

 ✅ In agent_loop.run(), wrap main steps in a rollback_if_tests_fail() context manager — this ensures unsafe patches aren’t committed if tests break

🚀 After That...
Once the planner is trend-aware, you’ll be ready to implement Phase 5: autonomous goal shaping based on GitHub trend evolution – but let’s crush Phase 4 first.

---

### 🔁 Phase 5 – Real-Time Monitoring & Auto PRs
**Goal:** Let the AI work completely hands-free

Features:
- Auto-push patches to new branch
- Auto-create PRs with metadata and patch
- Auto-label by type: `type:docs`, `enhancement`, etc.
- Webhook/CI-based feedback (e.g., only merge if tests pass)

---

## 🧑‍💻 Endgame

You become a **maintainer**, not an executor.  
TrendSpire:
- Suggests useful changes
- Opens pull requests
- You approve, tweak, or reject

It’s your open-source **co-pilot**, powered by Codex, and evolving with GitHub itself.

---
