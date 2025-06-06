import os
from pathlib import Path

from openai_call import improve_trending_md
from src.render_digest import update_readme


TRENDING_PATH = Path(__file__).resolve().parent.parent / "TRENDING.md"


def main() -> None:
    original_md = TRENDING_PATH.read_text(encoding="utf-8")
    improved_md = improve_trending_md(original_md)
    TRENDING_PATH.write_text(improved_md + "\n", encoding="utf-8")
    update_readme(improved_md)


if __name__ == "__main__":
    main()
