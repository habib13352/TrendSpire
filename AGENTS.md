# Agents

## TrendingFetcherAgent
**Description:** Periodically fetches GitHub’s trending repositories list.  
**Trigger:** Scheduled daily or on demand.  
**Prompt:** "Fetch today’s top 25 trending GitHub repositories in [language] and output as JSON."  
**Outputs:** `data/trending.json`

## PromptGeneratorAgent
**Description:** Generates engaging markdown content from the trending data.  
**Trigger:** After TrendingFetcherAgent completes.  
**Prompt:** "Given this list of trending repos, generate a human-friendly markdown summary with links and one-sentence descriptions."  
**Outputs:** `TRENDING.md`

## ReadmeUpdaterAgent
**Description:** Integrates the latest `TRENDING.md` into the project README.  
**Trigger:** After PromptGeneratorAgent completes or on PR.  
**Prompt:** "Insert or replace the ‘Trending This Week’ section in README.md with the contents of TRENDING.md, preserving existing headings."  
**Constraints:** Preserve other sections, log changes.

## CommitMessageAgent
**Description:** Crafts concise commit messages for all automated updates.  
**Prompt:** "Generate a present-tense, imperative commit message summarizing: {list of changed files or summary}."  
**Constraints:** Max 50 characters.

## PRCreatorAgent
**Description:** Automatically opens or updates a pull request with all changes.  
**Trigger:** After ReadmeUpdaterAgent runs.  
**Prompt:** "Open or update a PR on branch `auto/trending-update` with the following commit(s): {commit messages}, targeting `main`."  
**Outputs:** PR link in logs.

Each agent should log its actions to `logs/agents.log`.
