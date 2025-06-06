"""Simple helper for one-off OpenAI markdown improvements."""

import os
from openai import OpenAI

def improve_trending_md(original_md: str) -> str:
    """Return an improved version of the trending markdown using GPT-4."""
    prompt = f"""You are an expert technical content editor and GitHub influencer. Improve the following markdown by:
1. Making it more engaging and clear
2. Adding emojis or sections to improve readability
3. Making sure it's in a format that will attract GitHub stars
4. Suggesting any missing sections like tips, weekly highlights, or dev tools

Original markdown:
---
{original_md}
---

Improved markdown:"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
