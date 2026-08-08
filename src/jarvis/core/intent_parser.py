from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Intent:

    action: str
    target: str


class IntentParser:

    ACTIONS: ClassVar[dict[str, str]] = {
    # Open
    "open": "open",
    "launch": "open",
    "start": "open",
    "run": "open",

    # Close
    "close": "close",
    "exit": "close",
    "quit": "close",
    "stop": "close",
    "terminate": "close",
    "kill": "close",

    # Status
    "running": "status",
    "status": "status",
    "is": "status",
    }

    def parse(
        self,
        text: str,
    ) -> Intent | None:

        words = text.lower().split()

        if not words:
            return None

        action = self.ACTIONS.get(words[0])

        if action is None:
            return None

        target = " ".join(words[1:]).strip(
         " .,!?;:"
    )

        if not target:
            return None

        return Intent(
            action=action,
            target=target,
        )
