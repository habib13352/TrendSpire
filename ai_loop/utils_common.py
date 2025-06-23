import os
import subprocess
from datetime import datetime
from typing import Iterable, Optional

import tiktoken
from openai import OpenAI, OpenAIError


def load_prompt(template_name: str) -> str:
    """Return the contents of a prompt template under ai_loop/prompts."""
    path = os.path.join(os.path.dirname(__file__), "prompts", template_name)
    return open(path, "r", encoding="utf-8").read()


def ensure_logs(log_dir: str, cost_log: str, memory_dir: Optional[str] = None) -> None:
    """Create logging directories and cost file if missing."""
    os.makedirs(log_dir, exist_ok=True)
    if memory_dir:
        os.makedirs(memory_dir, exist_ok=True)
    if not os.path.exists(cost_log):
        with open(cost_log, "w", encoding="utf-8") as f:
            f.write("timestamp,run_type,prompt_tokens,completion_tokens,model,cost_usd\n")


def count_tokens(text: str, model: str) -> int:
    """Count tokens for the given model."""
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))


DEFAULT_MODEL = "gpt-4o"
MODEL_PRICES = {
    "gpt-4o": (0.005, 0.015),
    "gpt-4": (0.03, 0.06),
}


def call_openai_chat(
    messages: list[dict[str, str]], model: str = DEFAULT_MODEL
) -> tuple[str, int, int, float]:
    """Send messages to OpenAI Chat API and return text and usage."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in environment")

    client = OpenAI(api_key=api_key)
    try:
        resp = client.chat.completions.create(model=model, messages=messages)
    except OpenAIError as exc:
        raise RuntimeError(str(exc)) from exc

    content = resp.choices[0].message.content
    usage = resp.usage
    prompt_tokens = getattr(usage, "prompt_tokens", 0)
    completion_tokens = getattr(usage, "completion_tokens", 0)
    price = MODEL_PRICES.get(model, (0.0, 0.0))
    cost = (prompt_tokens / 1000 * price[0]) + (completion_tokens / 1000 * price[1])

    return content, prompt_tokens, completion_tokens, cost


def run_cmd(cmd: Iterable[str]) -> subprocess.CompletedProcess:
    """Run a shell command and capture output."""
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{proc.stderr}")
    return proc


def is_valid_diff(diff_text: str) -> bool:
    """Validate a unified diff for basic sanity."""
    lines = diff_text.strip().splitlines()

    # Must contain standard diff markers
    required_markers = any(
        line.startswith(("diff --git", "---", "+++", "@@")) for line in lines[:10]
    )
    if not required_markers:
        return False

    # Reject diffs touching tests/ directories
    for line in lines:
        if line.startswith(("diff --git", "---", "+++")):
            parts = line.split()
            for part in parts[2:4]:
                part = part.replace("a/", "").replace("b/", "")
                if part.startswith("tests/") or "/tests/" in part:
                    return False

    # Reject excessive deletions
    deletions = sum(1 for line in lines if line.startswith("-") and not line.startswith("---"))
    if deletions > 50:
        return False

    return True


def is_suspicious_deletion(diff_text: str) -> bool:
    """Return True if the diff removes entire files."""
    lines = diff_text.splitlines()
    return any("deleted file mode" in line for line in lines)


def append_cost(timestamp: str, run_type: str, tokens: tuple[int, int], model: str, cost: float, cost_log: str) -> None:
    """Append cost information to CSV log."""
    prompt_tokens, completion_tokens = tokens
    with open(cost_log, "a", encoding="utf-8") as f:
        f.write(f"{timestamp},{run_type},{prompt_tokens},{completion_tokens},{model},{cost:.6f}\n")


def write_summary(path: str, model: str, run_type: str, tokens: tuple[int, int], cost: float, test_output: str, diff_snippet: str) -> None:
    """Write markdown summary report."""
    prompt_tokens, completion_tokens = tokens
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"## {run_type.capitalize()} Codex Run {datetime.utcnow().isoformat()}\n\n")
        f.write(f"Model: {model}\n\n")
        f.write(f"Prompt tokens: {prompt_tokens}\n")
        f.write(f"Completion tokens: {completion_tokens}\n")
        f.write(f"Cost: ${cost:.6f}\n\n")
        f.write("### Test Output\n")
        f.write(f"```\n{test_output}\n```\n")
        f.write("### Diff Snippet\n")
        f.write(f"```diff\n{diff_snippet}\n```\n")


def rollback_if_tests_fail() -> subprocess.CompletedProcess:
    """Run ai_loop tests and rollback the last commit if they fail."""
    result = subprocess.run(
        ["pytest", "ai_loop/tests/"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if result.returncode != 0:
        subprocess.run(["git", "reset", "--hard", "HEAD~1"], check=False)
        raise RuntimeError("Tests failed after patch; rolled back.")
    return result
