from __future__ import annotations

from pathlib import Path

BAD_EXECUTABLES = {
    "unins000.exe",
    "uninstall.exe",
    "setup.exe",
    "update.exe",
    "updater.exe",
    "msiexec.exe",
}


class ExecutableResolver:

    def resolve(
        self,
        app_name: str,
        install_location: str,
    ) -> str:

        if not install_location:
            return ""

        folder = Path(install_location)

        if not folder.exists():
            return ""

        executables = []

        for exe in folder.rglob("*.exe"):

            if exe.name.lower() in BAD_EXECUTABLES:
                continue

            executables.append(exe)

        if not executables:
            return ""

        app_words = {word.lower() for word in app_name.split() if len(word) > 2}

        scored = []

        for exe in executables:

            score = 0

            filename = exe.stem.lower()

            for word in app_words:

                if word in filename:
                    score += 10

            score += exe.stat().st_size / 1_000_000

            scored.append((score, exe))

        scored.sort(
            reverse=True,
            key=lambda x: x[0],
        )

        return str(scored[0][1])
