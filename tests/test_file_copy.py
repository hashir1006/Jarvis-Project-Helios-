import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.file_operations import FileOperations


def test_copy(tmp_path):

    operations = FileOperations()

    source = tmp_path / "source.txt"
    destination = tmp_path / "copy.txt"

    source.write_text("Hello Project Helios")

    assert operations.copy(
        source,
        destination,
    )

    assert destination.exists()

    assert destination.read_text() == source.read_text()
