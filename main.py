import os
import sys
import argparse
from readme_loader import load_readme
from improver import (
    generate_summary,
    suggest_improvements,
    rewrite_readme,
    load_config,
)
from logger import get_logger

logger = get_logger()


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(prog="ai-readme-improver")
    parser.add_argument("--config", default="config.yaml", help="Path to config file")
    parser.add_argument("--email", help="Override contact email")
    parser.add_argument("--logo-path", help="Override logo path")
    parser.add_argument("--dry-run", action="store_true", help="Print settings but do not call OpenAI")
    parser.add_argument("--interactive", action="store_true", help="Prompt for config values interactively")
    args = parser.parse_args()

    config = load_config(args.config)

    if args.interactive:
        print("🚀  AI README Improver Configuration Wizard")
        project_name = input("1) Enter project name: ").strip()
        email_input = input("2) Enter contact email: ").strip()
        logo_input = input("3) Enter logo path (e.g. assets/logo.png): ").strip()
        if project_name:
            config["project_name"] = project_name
        if email_input:
            config["email"] = email_input
        if logo_input:
            config["logo_path"] = logo_input

    if args.email:
        config["email"] = args.email
    if args.logo_path:
        config["logo_path"] = args.logo_path

    if args.dry_run:
        print("[DRY RUN] Final config:", config)
        sys.exit(0)

    if not os.getenv("OPENAI_API_KEY"):
        logger.error("OPENAI_API_KEY is not set. Add it to your .env file.")
        return

    readme_path = "README.md"
    if not os.path.exists(readme_path):
        logger.error(f"❌ Error: {readme_path} not found.")
        return

    readme_text = load_readme(readme_path)
    if not readme_text.strip():
        logger.warning("⚠️ README is empty. Exiting.")
        return

    logger.info("🔹 Generating TL;DR summary...")
    summary = generate_summary(readme_text)
    logger.info("\n--- TL;DR SUMMARY ---\n")
    logger.info(summary)
    logger.info("\n----------------------\n")

    logger.info("🔹 Generating improvement suggestions...")
    suggestions = suggest_improvements(readme_text)
    logger.info("\n--- IMPROVEMENT SUGGESTIONS ---\n")
    logger.info(suggestions)
    logger.info("\n--------------------------------\n")

    with open("suggestions.md", "w", encoding="utf-8") as f:
        f.write("# 🤖 AI README Improver Feedback\n\n")
        f.write("## TL;DR Summary\n\n")
        f.write(summary.strip() + "\n\n")
        f.write("## Improvement Suggestions\n\n")
        f.write(suggestions.strip() + "\n\n")
        f.write("---\n*Powered by [OpenAI](https://openai.com)*\n")
    logger.info("✅ Wrote feedback to suggestions.md")

    logger.info("🔹 Generating rewritten README → README.improved.md")
    improved = rewrite_readme(readme_text, config)
    with open("README.improved.md", "w", encoding="utf-8") as f:
        f.write(improved)
    logger.info("✅ Saved improved version to README.improved.md\n")


if __name__ == "__main__":
    main()
