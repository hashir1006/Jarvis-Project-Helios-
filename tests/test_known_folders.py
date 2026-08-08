import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.file_manager import FileManager


def test_known_folders():

    manager = FileManager()

    downloads = manager.resolve("downloads")

    print(downloads)

    assert downloads is not None
    assert downloads.exists()

    files = manager.list("downloads")

    print(f"Downloads contains {len(files)} items")
