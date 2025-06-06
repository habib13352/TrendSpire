#!/bin/bash
# Verify repository state after automated commit and push
set -e

EXPECTED_MSG="\xF0\x9F\x94\x84 Auto-update README and TRENDING"

if [[ -n $(git status --porcelain) ]]; then
  echo "Repository has uncommitted changes" >&2
  exit 1
fi

last_msg=$(git log -1 --pretty=%B)
if [[ "$last_msg" != "$EXPECTED_MSG"* ]]; then
  echo "Unexpected commit message: $last_msg" >&2
  exit 1
fi

if ! git push; then
  echo "Git push failed" >&2
  if [[ -n "$GITHUB_TOKEN" ]]; then
    repo=$(git config --get remote.origin.url | sed -E 's#.*/(.*/.*)\.git#\1#')
    curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
      -d "{\"title\":\"Automation push failed\",\"body\":\"Push failed on $(date).\"}" \
      "https://api.github.com/repos/$repo/issues" >/dev/null
  fi
  exit 1
fi

echo "Commit and push verified"
