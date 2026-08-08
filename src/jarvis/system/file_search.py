from __future__ import annotations

from pathlib import Path


class FileSearch:

    def search(
        self,
        root: Path,
        query: str,
    ) -> list[Path]:

        matches: list[Path] = []

        query = query.lower()

        if not root.exists():
            return matches

        for path in root.rglob("*"):

            try:

                if query in path.name.lower():
                    matches.append(path)

            except OSError:
                continue

        return matches
