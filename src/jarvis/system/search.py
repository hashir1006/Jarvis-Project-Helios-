from __future__ import annotations

import json
from pathlib import Path

from jarvis.system.search_engine import SearchEngine


class ApplicationSearch:

    def __init__(self):

        self.cache = Path("runtime/cache/application_index.json")

        self.aliases = Path("config/application_aliases.json")

        self.engine = SearchEngine()

    def _resolve_alias(
        self,
        query: str,
    ) -> str:

        print(f"Aliases file exists: {self.aliases.exists()}")
        print(f"Aliases path: {self.aliases.resolve()}")

        if not self.aliases.exists():
            return query

        with open(
            self.aliases,
            "r",
            encoding="utf-8",
        ) as file:

            aliases = json.load(file)

        return aliases.get(
            query.lower(),
            query,
        )

    def search(
        self,
        query: str,
    ) -> list[dict]:

        if not self.cache.exists():
            raise FileNotFoundError("Run: python scripts/dev.py index")

        query = self._resolve_alias(query)

        print(f"Resolved query: {query}")

        with open(
            self.cache,
            "r",
            encoding="utf-8",
        ) as file:

            applications = json.load(file)

        ranked = []

        for app in applications:

            name = app.get(
                "name",
                "",
            )

            score = self.engine.score(
                query,
                name,
            )

            # Debug only
            if "Visual Studio Code" in name:
                print(f"\nCandidate : {name}")
                print(f"Score     : {score}")

            if score >= 60:
                ranked.append(
                    (
                        score,
                        app,
                    )
                )

        ranked.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return [app for score, app in ranked]
