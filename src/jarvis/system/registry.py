from __future__ import annotations

import winreg
from pathlib import Path

from jarvis.system.models import Application
from jarvis.interfaces.base_scanner import BaseScanner


UNINSTALL_KEYS = (
    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
    r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall",
)


class RegistryScanner(BaseScanner):

    def scan(self) -> list[Application]:
        apps: list[Application] = []

        hives = (
            winreg.HKEY_LOCAL_MACHINE,
            winreg.HKEY_CURRENT_USER,
        )

        for hive in hives:

            for uninstall_key in UNINSTALL_KEYS:

                try:
                    key = winreg.OpenKey(hive, uninstall_key)
                except OSError:
                    continue

                subkeys = winreg.QueryInfoKey(key)[0]

                for i in range(subkeys):

                    try:
                        subkey_name = winreg.EnumKey(key, i)

                        subkey = winreg.OpenKey(key, subkey_name)

                        name = self._read(subkey, "DisplayName")

                        if not name:
                            continue

                        install_location = self._read(
                            subkey,
                            "InstallLocation"
                        )

                        publisher = self._read(
                            subkey,
                            "Publisher"
                        )

                        version = self._read(
                            subkey,
                            "DisplayVersion"
                        )

                        uninstall_string = self._read(
                            subkey,
                            "UninstallString"
                        )

                        apps.append(
                            Application(
                                name=name,
                                executable=uninstall_string or "",
                                install_path=Path(
                                    install_location or ""
                                ),
                                publisher=publisher,
                                version=version,
                            )
                        )

                    except OSError:
                        continue

        return apps

    @staticmethod
    def _read(key, value):

        try:
            return winreg.QueryValueEx(key, value)[0]
        except OSError:
            return None