from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CommandResult:
    success: bool
    message: str