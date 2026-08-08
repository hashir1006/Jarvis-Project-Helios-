from __future__ import annotations

from pathlib import Path

from jarvis.interfaces.base_scanner import BaseScanner
from jarvis.system.models import Application

START_MENU_PATHS = [
    Path(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"),
    Path.home() / r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs",
]


class StartMenuScanner(BaseScanner):

    def scan(self) -> list[Application]:

        applications: list[Application] = []

        for base in START_MENU_PATHS:

            if not base.exists():
                continue

            for shortcut in base.rglob("*.lnk"):

                applications.append(
                    Application(
                        name=shortcut.stem,
                        executable=str(shortcut),
                        install_path=shortcut.parent,
                    )
                )

        return applications
