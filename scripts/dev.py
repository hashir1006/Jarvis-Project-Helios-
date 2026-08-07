from pathlib import Path
import sys
import argparse

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.application_indexer import ApplicationIndexer
from jarvis.system.search import ApplicationSearch
from jarvis.system.launcher import ApplicationLauncher


def main():

    parser = argparse.ArgumentParser(
        prog="JARVIS Developer CLI",
        description="Developer tools for JARVIS OS",
    )

    parser.add_argument(
        "command",
        nargs="?",
        default="help",
        help="Developer command",
    )

    parser.add_argument(
        "argument",
        nargs="?",
        help="Optional command argument",
    )

    args = parser.parse_args()

    match args.command:

        case "help":
            print("""
=========================
JARVIS Developer CLI
=========================

Available commands

help
index
search <application>
open <application>
""")

        case "index":
            ApplicationIndexer().build()

        case "search":

            if not args.argument:
                print("Usage: python scripts/dev.py search <application>")
                return

            search = ApplicationSearch()

            results = search.search(args.argument)

            if not results:
                print("No matching applications found.")
                return

            print(f"\nFound {len(results)} application(s):\n")

            for i, app in enumerate(results, start=1):
                print(f"[{i}] {app['name']}")
                print(f"    Path: {app['install_path']}")
                print()

        case "open":

            if not args.argument:
                print("Usage: python scripts/dev.py open <application>")
                return

            launcher = ApplicationLauncher()
            launcher.open(args.argument)

        case _:
            print(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()