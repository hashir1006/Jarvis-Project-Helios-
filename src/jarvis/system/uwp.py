from __future__ import annotations

import json
import subprocess
from pathlib import Path

from jarvis.interfaces.base_scanner import BaseScanner
from jarvis.system.models import Application


class UWPScanner(BaseScanner):

    def scan(self) -> list[Application]:

        command = [
            "powershell",
            "-NoProfile",
            "-Command",
            "Get-StartApps | Select-Object Name,AppID | ConvertTo-Json",
        ]

        try:

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
            )

        except subprocess.SubprocessError:

            return []

        if not result.stdout.strip():
            return []

        data = json.loads(result.stdout)

        if isinstance(data, dict):
            data = [data]

        applications: list[Application] = []

        for item in data:

            name = item.get("Name")
            appid = item.get("AppID")

            if not name or not appid:
                continue

            applications.append(
                Application(
                    name=name,
                    executable=appid,
                    install_path=Path("."),
                    category="uwp",
                )
            )

        return applications
