import argparse
from pathlib import Path
import logging


def run_fetch(_args: argparse.Namespace) -> None:
    """Fetch trending repos and update README."""
    from .fetch import render_trending, update_readme

    print("Fetching trending repositories...")
    logging.info("Fetching trending repositories...")
    markdown = render_trending()
    update_readme(markdown)
    print("Trending digest updated.")
    logging.info("Trending digest updated.")


def run_ai_patch(args: argparse.Namespace) -> None:
    """Generate an improved README using OpenAI."""
    from . import ai_patch

    print("Running AI README improver...")
    logging.info("Running AI README improver...")
    config = ai_patch.load_config(args.config)
    text = Path(args.readme).read_text(encoding="utf-8")
    improved = ai_patch.rewrite_readme(text, config)
    Path(args.output).write_text(improved, encoding="utf-8")
    print(f"Wrote improved README to {args.output}")
    logging.info(f"Wrote improved README to {args.output}")


def run_ai_readme(args: argparse.Namespace) -> None:
    """Improve README using ai_loop.ai_readme."""
    from . import ai_readme

    print("Running AI README updater...")
    logging.info("Running AI README updater...")
    success = ai_readme.improve_readme(enable=args.enable)
    if success:
        print("README updated.")
        logging.info("README updated.")
    else:
        print("README unchanged.")
        logging.info("README unchanged.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="trendspire")
    sub = parser.add_subparsers(dest="command", required=True)

    fetch_p = sub.add_parser("fetch", help="Fetch trending repos and update README")
    fetch_p.set_defaults(func=run_fetch)

    patch_p = sub.add_parser("ai-patch", help="Run AI README improver")
    patch_p.add_argument("--config", default="config.yaml", help="Path to config file")
    patch_p.add_argument("--readme", default="README.md", help="README to improve")
    patch_p.add_argument("--output", default="README.improved.md", help="Output file")
    patch_p.set_defaults(func=run_ai_patch)

    readme_p = sub.add_parser("ai-readme", help="Update README with trending summary")
    readme_p.add_argument("--enable", action="store_true", help="Run the updater")
    readme_p.set_defaults(func=run_ai_readme)

    return parser


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
