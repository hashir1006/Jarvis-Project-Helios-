from __future__ import annotations
from pathlib import Path

import psutil


class ProcessManager:

    def list_processes(self) -> list[psutil.Process]:

        processes = []

        for process in psutil.process_iter(
            [
                "pid",
                "name",
                "exe",
            ]
        ):
            try:
                processes.append(process)

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
            ):
                continue

        return processes

    def is_running(
        self,
        query: str,
    ) -> bool:

        query = query.lower()

        for process in self.list_processes():

            try:

                name = (process.info["name"] or "").lower()

                exe = (process.info["exe"] or "").lower()

                if query in name:
                    return True

                if query in exe:
                    return True

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
            ):
                continue

        return False

    def close(
    self,
    query: str,
) -> int:

        query = query.lower().strip()

        closed = 0

        for process in self.list_processes():

            try:

                name = (
                    process.info["name"] or ""
                ).lower()

                exe = (
                    process.info["exe"] or ""
                ).lower()

                if (
                    query == name
                     or query == Path(name).stem
                     or query in exe
                ):

                    print(
                        f"[ProcessManager] Closing: "
                        f"{name} "
                        f"(PID {process.pid})"
                    )

                    process.terminate()

                    try:
                        process.wait(
                            timeout=5
                        )

                    except psutil.TimeoutExpired:

                        print(
                            f"[ProcessManager] "
                            f"Force killing PID {process.pid}"
                        )

                        process.kill()
                        process.wait(timeout=3)

                    closed += 1

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
            ):
                continue

        print(
            f"[ProcessManager] Closed {closed} process(es)."
        )

        return closed