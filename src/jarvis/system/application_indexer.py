from __future__ import annotations

import json
import re
from dataclasses import asdict
from pathlib import Path

from jarvis.interfaces.base_scanner import BaseScanner
from jarvis.system.registry import RegistryScanner
from jarvis.system.startmenu import StartMenuScanner
from jarvis.system.uwp import UWPScanner

BAD_KEYWORDS = {
    "uninstall",
    "uninstaller",
    "install",
    "installer",
    "setup",
    "repair",
    "modify",
    "update",
    "readme",
    "license",
    "documentation",
    "codec",
    "redistributable",
    "runtime",
    "minimum runtime",
    "additional runtime",
}


class ApplicationIndexer:

    def __init__(self):

        self.scanners: list[BaseScanner] = [
            RegistryScanner(),
            StartMenuScanner(),
            UWPScanner(),
        ]

    def build(self):

        applications = []

        # -----------------------------
        # Scan applications
        # -----------------------------

        for scanner in self.scanners:

            print(f"Running {scanner.__class__.__name__}...")

            results = scanner.scan()

            print(f"{scanner.__class__.__name__}: {len(results)} applications")

            for app in results:
                if "calculator" in app.name.lower():
                    print("FOUND CALCULATOR:")
                    print(app)

            applications.extend(results)

        print(f"\nTotal scanned: {len(applications)}")

        # -----------------------------
        # Filter unwanted entries
        # -----------------------------

        filtered = []

        for app in applications:

            name = app.name.lower()

            if any(keyword in name for keyword in BAD_KEYWORDS):
                continue

            filtered.append(app)

        print(f"After filtering: {len(filtered)}")

        # -----------------------------
        # Remove duplicates
        # -----------------------------

        unique = {}

        for app in filtered:

            key = self.normalize_name(app.name)

            if key not in unique:
                unique[key] = app

        applications = list(unique.values())

        print(f"After deduplication: {len(applications)}")

        # -----------------------------
        # Verify Calculator survived
        # -----------------------------

        found = False

        for app in applications:

            if "calculator" in app.name.lower():
                print("\nCalculator survived:")
                print(app)
                found = True

        if not found:
            print("\nCalculator NOT found after deduplication.")

        # -----------------------------
        # Write cache
        # -----------------------------

        cache = Path("runtime/cache/application_index.json")

        cache.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        data = []

        for app in applications:

            item = asdict(app)
            item["install_path"] = str(app.install_path)

            data.append(item)

        cache.write_text(
            json.dumps(
                data,
                indent=4,
            ),
            encoding="utf-8",
        )

        print(f"\nIndexed {len(applications)} applications.")

        return applications

    @staticmethod
    def normalize_name(
        name: str,
    ) -> str:

        name = name.lower()

        # Remove text inside brackets
        name = re.sub(
            r"\(.*?\)",
            "",
            name,
        )

        # Remove vendor prefixes
        prefixes = (
            "microsoft ",
            "google ",
        )

        for prefix in prefixes:
            name = name.removeprefix(prefix)

        # Collapse whitespace
        name = " ".join(name.split())

        return name
