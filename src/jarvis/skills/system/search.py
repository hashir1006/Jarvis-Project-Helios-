from __future__ import annotations

import json
from pathlib import Path


class ApplicationSearch:

    def __init__(self):
        self.cache = Path("runtime/cache/application_index.json")

    def search(self, query: str) -> list[dict]:

        if not self.cache.exists():
            raise FileNotFoundError(
                "Application index not found. Run: python scripts/dev.py index"
            )

        with open(self.cache, "r", encoding="utf-8") as f:
            apps = json.load(f)

        query = query.lower()

        matches = []

        for app in apps:

            name = app.get("name", "").lower()

            if query in name:
                matches.append(app)

        return matches
