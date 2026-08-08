import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.core.command_dispatcher import CommandDispatcher
from jarvis.core.intent_parser import Intent


def test_dispatcher():

    dispatcher = CommandDispatcher()

    intent = Intent(
        action="status",
        target="explorer",
    )

    result = dispatcher.dispatch(intent)

    print(result)

    assert result is True
