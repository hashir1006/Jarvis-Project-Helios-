from __future__ import annotations

from jarvis.core.command_result import CommandResult
from jarvis.core.intent_parser import Intent
from jarvis.system.application_manager import ApplicationManager


class CommandDispatcher:

    def __init__(self):

        self.apps = ApplicationManager()

    def dispatch(
        self,
        intent: Intent,
    ) -> CommandResult:

        match intent.action:

            case "open":

                success = self.apps.open(intent.target)

                if success:
                    return CommandResult(
                        success=True,
                        message=f"Opening {intent.target}.",
                    )

                return CommandResult(
                    success=False,
                    message=f"I couldn't open {intent.target}.",
                )

            case "close":

                success = self.apps.close(intent.target)

                if success:
                    return CommandResult(
                        success=True,
                        message=f"Closing {intent.target}.",
                    )

                return CommandResult(
                    success=False,
                    message=f"I couldn't close {intent.target}.",
                )

            case "status":

                running = self.apps.is_running(intent.target)

                if running:
                    return CommandResult(
                        success=True,
                        message=f"{intent.target} is running.",
                    )

                return CommandResult(
                    success=True,
                    message=f"{intent.target} is not running.",
                )

            case _:

                return CommandResult(
                    success=False,
                    message=f"I don't know how to {intent.action} {intent.target}.",
                )