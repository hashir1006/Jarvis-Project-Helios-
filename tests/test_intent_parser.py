import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.core.intent_parser import IntentParser


def test_parser():

    parser = IntentParser()

    commands = [
        "open chrome",
        "launch code",
        "close spotify",
        "start notepad",
    ]

    for command in commands:

        intent = parser.parse(command)

        print(command, "->", intent)

        assert intent is not None
