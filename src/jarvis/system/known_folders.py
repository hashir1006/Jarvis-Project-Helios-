from __future__ import annotations

from pathlib import Path


class KnownFolders:

    @staticmethod
    def home() -> Path:
        return Path.home()

    @staticmethod
    def desktop() -> Path:
        return Path.home() / "Desktop"

    @staticmethod
    def documents() -> Path:
        return Path.home() / "Documents"

    @staticmethod
    def downloads() -> Path:
        return Path.home() / "Downloads"

    @staticmethod
    def pictures() -> Path:
        return Path.home() / "Pictures"

    @staticmethod
    def videos() -> Path:
        return Path.home() / "Videos"

    @staticmethod
    def music() -> Path:
        return Path.home() / "Music"

    @classmethod
    def resolve(cls, name: str) -> Path | None:

        folders = {
            "home": cls.home(),
            "desktop": cls.desktop(),
            "documents": cls.documents(),
            "downloads": cls.downloads(),
            "pictures": cls.pictures(),
            "videos": cls.videos(),
            "music": cls.music(),
        }

        return folders.get(name.lower())
