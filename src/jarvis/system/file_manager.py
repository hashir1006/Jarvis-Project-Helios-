from __future__ import annotations

import os
from pathlib import Path

from jarvis.system.known_folders import KnownFolders


class FileManager:

    def open_folder(
        self,
        folder: str,
    ) -> bool:

        path = self.resolve(folder)

        if path is None:
            return False

        if not path.exists():
            return False

        os.startfile(path)

        return True

    def exists(
        self,
        path: str | Path,
    ) -> bool:

        return Path(path).exists()

    def list(
        self,
        folder: str | Path,
    ) -> list[Path]:

        if isinstance(folder, str):

            known = KnownFolders.resolve(folder)

            if known is not None:
                folder = known

        folder = Path(folder)

        if not folder.exists():
            return []

        return list(folder.iterdir())

    def resolve(
        self,
        name: str,
    ) -> Path | None:

        return KnownFolders.resolve(name)
