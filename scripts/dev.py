from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.application_manager import ApplicationManager


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

    manager = ApplicationManager()

    match args.command:

        case "help":

            print("""
Available commands

help
index
search <application>
open <application>
""")

        case "index":

            manager.index()

        case "search":

            if not args.argument:
                print("Usage: python scripts/dev.py search <application>")
                return

            results = manager.search(args.argument)

            if not results:
                print("No matching applications found.")
                return

            print(f"\nFound {len(results)} application(s):\n")

            for i, app in enumerate(results, start=1):

                print(f"[{i}] {app['name']}")

                if app.get("category") == "uwp":
                    print("    Type: Microsoft Store App")
                else:
                    print(f"    Path: {app['install_path']}")

                print()

        case "open":

            if not args.argument:
                print("Usage: python scripts/dev.py open <application>")
                return

            manager.open(args.argument)

        case _:

            print(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
