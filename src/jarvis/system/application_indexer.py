import json
from dataclasses import asdict
from pathlib import Path

from jarvis.interfaces.base_scanner import BaseScanner
from jarvis.system.registry import RegistryScanner
from jarvis.system.startmenu import StartMenuScanner


class ApplicationIndexer:

    def __init__(self):
        self.scanners: list[BaseScanner] = [
            RegistryScanner(),
            StartMenuScanner(),
        ]

    def build(self):

        applications = []

        for scanner in self.scanners:
            print(f"Running {scanner.__class__.__name__}...")
            applications.extend(scanner.scan())

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