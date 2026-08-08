from __future__ import annotations

import os
import subprocess
from pathlib import Path

from jarvis.system.search import ApplicationSearch


class ApplicationLauncher:

    def __init__(self):
        self.search = ApplicationSearch()

    def open(
        self,
        query: str,
    ) -> bool:

        results = self.search.search(query)

        if not results:
            print(f"No application found for '{query}'.")
            return False

        app = results[0]

        executable = app.get(
            "executable",
            "",
        )

        category = app.get(
            "category",
            "",
        )

        if not executable:
            print("Executable information is unavailable.")
            return False

        executable = executable.strip('"')

        try:

            # -----------------------------
            # Microsoft Store / UWP apps
            # -----------------------------
            if category == "uwp":

                subprocess.Popen(
                    [
                        "explorer.exe",
                        f"shell:AppsFolder\\{executable}",
                    ]
                )

            # -----------------------------
            # Win32 applications
            # -----------------------------
            else:

                path = Path(executable)

                if path.exists():
                    os.startfile(path)
                else:
                    subprocess.Popen(executable)

            print(f"Launched: {app['name']}")
            return True

        except (FileNotFoundError, OSError, subprocess.SubprocessError) as error:

            print(f"Launch failed: {error}")
            return False
