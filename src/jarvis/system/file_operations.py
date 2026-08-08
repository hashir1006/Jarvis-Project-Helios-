from __future__ import annotations

import os
import shutil
from pathlib import Path

from send2trash import send2trash


class FileOperations:

    def open(
        self,
        path: str | Path,
    ) -> bool:

        path = Path(path)

        if not path.exists():
            return False

        os.startfile(path)

        return True

    def rename(
        self,
        source: str | Path,
        destination: str | Path,
    ) -> bool:

        source = Path(source)
        destination = Path(destination)

        if not source.exists():
            return False

        try:
            source.rename(destination)

            return True

        except OSError:

            return False

    def copy(
        self,
        source: str | Path,
        destination: str | Path,
    ) -> bool:

        source = Path(source)
        destination = Path(destination)

        if not source.exists():
            return False

        try:

            shutil.copy2(
                source,
                destination,
            )

            return True

        except OSError:

            return False

    def move(
        self,
        source: str | Path,
        destination: str | Path,
    ) -> bool:

        source = Path(source)
        destination = Path(destination)

        if not source.exists():
            return False

        try:

            shutil.move(
                source,
                destination,
            )

            return True

        except OSError:

            return False

    def create_folder(
        self,
        path: str | Path,
    ) -> bool:

        path = Path(path)

        try:

            path.mkdir(
                parents=True,
                exist_ok=True,
            )

            return True

        except OSError:

            return False

    def delete(
        self,
        path: str | Path,
    ) -> bool:

        path = Path(path)

        if not path.exists():
            return False

        try:

            send2trash(path)

            return True

        except OSError:

            return False
