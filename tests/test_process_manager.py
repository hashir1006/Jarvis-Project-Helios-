import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.process_manager import ProcessManager


def test_process_manager():

    manager = ProcessManager()

    print(f"\nProcesses: {len(manager.list_processes())}")

    print("Explorer:", manager.is_running("explorer"))
    print("Code:", manager.is_running("code"))
    print("Chrome:", manager.is_running("chrome"))

    assert manager.is_running("explorer") is True
