import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.application_manager import ApplicationManager


def test_application_manager():

    manager = ApplicationManager()

    print("\nSearching for Chrome...")
    print(manager.search("chrome"))

    print("\nIs Explorer Running?")
    print(manager.is_running("explorer"))

    assert manager.is_running("explorer") is True
