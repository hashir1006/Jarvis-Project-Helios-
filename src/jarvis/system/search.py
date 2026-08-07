from __future__ import annotations

import json
from pathlib import Path


class ApplicationSearch:

    def __init__(self):
        self.cache = Path("runtime/cache/application_index.json")

    def search(self, query: str) -> list[dict]:

        if not self.cache.exists():
            raise FileNotFoundError(
                "Run: python scripts/dev.py index"
            )

        with open(self.cache, "r", encoding="utf-8") as file:
            applications = json.load(file)

        query = query.lower()

        return [
            app
            for app in applications
            if query in app.get("name", "").lower()
        ]