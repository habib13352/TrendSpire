import argparse
import logging
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Iterable

from openai import OpenAI

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ai_loop.utils_common import load_prompt, rollback_if_tests_fail


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

LOG_DIR = Path("ai_loop/codex_logs")
LOG_DIR.mkdir(exist_ok=True)


logging.basicConfig(
    filename=LOG_DIR / f"log_{datetime.utcnow().isoformat()}.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_analysis_prompt(file_path: str, code: str) -> str:
    language = Path(file_path).suffix.lstrip(".") or "text"
    template = load_prompt("autobot.j2")
    return (
        template.replace("{{ file_path }}", file_path)
        .replace("{{ language }}", language)
        .replace("{{ code }}", code)
    )




def get_target_files(folder: str = "src", exts: Iterable[str] = ("py",), days: int | None = None, min_size: int = 0) -> list[str]:
    """Return files under *folder* matching extensions and filters."""
    cutoff = None
    if days is not None:
        cutoff = datetime.utcnow() - timedelta(days=days)
    results: list[str] = []
    for path in Path(folder).rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lstrip(".") not in exts:
            continue
        if path.name.startswith("_"):
            continue
        stat = path.stat()
        if cutoff and datetime.utcfromtimestamp(stat.st_mtime) < cutoff:
            continue
        if stat.st_size < min_size:
            continue
        results.append(str(path))
    return results


def create_branch(branch_name: str) -> None:
    subprocess.run(["git", "checkout", "-b", branch_name], check=True)


def commit_and_push(file_paths: list[str], branch_name: str) -> None:
    for f in file_paths:
        subprocess.run(["git", "add", f], check=True)
    subprocess.run(["git", "commit", "-m", f"Codex Bot: Improve {', '.join(file_paths)}"], check=True)
    try:
        rollback_if_tests_fail()
    except RuntimeError as exc:
        logging.error(str(exc))
        return
    subprocess.run(["git", "push", "origin", branch_name], check=True)


def create_pr(pr_title: str, pr_body: str) -> None:
    subprocess.run([
        "gh",
        "pr",
        "create",
        "--base",
        "main",
        "--head",
        "codex-bot",
        "--title",
        pr_title,
        "--body",
        pr_body,
    ], check=True)


def call_gpt(prompt: str) -> str:
    logging.info("Calling OpenAI API...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Codex Autobot")
    parser.add_argument("--extensions", "-e", nargs="+", default=["py"], help="File extensions to scan")
    parser.add_argument("--days", type=int, default=None, help="Only files modified within N days")
    parser.add_argument("--min-size", type=int, default=0, help="Skip files smaller than this size (bytes)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    modified_files: list[str] = []
    pr_summary: list[str] = []

    files = get_target_files("src", args.extensions, args.days, args.min_size)
    if not files:
        logging.info("No target files found.")
        return

    branch_name = "codex-bot"
    create_branch(branch_name)

    for file in files:
        original_code = Path(file).read_text()
        prompt = get_analysis_prompt(file, original_code)
        result = call_gpt(prompt)

        if "```" in result:
            try:
                new_code = result.split("```", 1)[1].split("```", 1)[0].strip()
                if new_code != original_code:
                    Path(file).write_text(new_code)
                    modified_files.append(file)
                    pr_summary.append(result.split("🛠️ Suggested improvements", 1)[-1].split("🧠 Rewritten code")[0].strip())
                    logging.info(f"Updated file: {file}")
            except Exception as exc:
                logging.error(f"Error processing file {file}: {exc}")

    if modified_files:
        commit_and_push(modified_files, branch_name)
        pr_title = "Codex Autobot Improvements"
        pr_body = "\n".join(pr_summary)
        create_pr(pr_title, pr_body)
        logging.info("PR created successfully.")
    else:
        logging.info("No changes suggested.")


if __name__ == "__main__":
    main()
