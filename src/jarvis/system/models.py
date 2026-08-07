from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Application:

    name: str

    executable: str

    install_path: Path

    version: str | None = None

    publisher: str | None = None

    category: str | None = None

    icon: str | None = None

    capabilities: list[str] | None = None