import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.file_manager import FileManager


def test_open_folder():

    manager = FileManager()

    assert manager.open_folder("downloads") is True
