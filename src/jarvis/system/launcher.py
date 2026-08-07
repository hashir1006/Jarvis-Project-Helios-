from __future__ import annotations

import subprocess
from pathlib import Path

from jarvis.system.search import ApplicationSearch


class ApplicationLauncher:

    def __init__(self):
        self.search = ApplicationSearch()

    def open(self, query: str) -> bool:

        results = self.search.search(query)

        if not results:
            print(f"No application found for '{query}'.")
            return False

        app = results[0]

        executable = app.get("executable", "")

        if not executable:
            print("Executable information is unavailable.")
            return False

        executable = executable.strip('"')

        path = Path(executable)

        try:
            if path.exists():
                subprocess.Popen([str(path)])
            else:
                subprocess.Popen(executable)

            print(f"Launched: {app['name']}")
            return True

        except Exception as e:
            print(f"Launch failed: {e}")
            return False