import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.file_operations import FileOperations


def test_open_file():

    operations = FileOperations()

    from pathlib import Path

    result = operations.open(Path.home() / "Downloads")

    assert result is True
