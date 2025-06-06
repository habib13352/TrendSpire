"""Load a README file and return its contents."""

from __future__ import annotations

from pathlib import Path
from typing import Union


def load_readme(path: Union[str, Path] = "README.md") -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        return ""
