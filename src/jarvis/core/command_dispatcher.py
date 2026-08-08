from __future__ import annotations

from jarvis.core.intent_parser import Intent
from jarvis.system.application_manager import ApplicationManager


class CommandDispatcher:

    def __init__(self):

        self.apps = ApplicationManager()

    def dispatch(
        self,
        intent: Intent,
    ):

        match intent.action:

            case "open":
                return self.apps.open(intent.target)

            case "close":
                return self.apps.close(intent.target)

            case "status":
                return self.apps.is_running(intent.target)

            case _:
                raise ValueError(f"Unknown action: {intent.action}")
