import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.file_manager import FileManager


def test_file_manager():

    manager = FileManager()

    assert manager.exists(Path.home())

    files = manager.list(Path.home())

    print(f"\nFound {len(files)} items")

    assert isinstance(files, list)
