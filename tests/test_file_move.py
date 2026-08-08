import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.file_operations import FileOperations


def test_move(tmp_path):

    operations = FileOperations()

    source = tmp_path / "old.txt"
    destination = tmp_path / "new.txt"

    source.write_text("Project Helios")

    assert operations.move(
        source,
        destination,
    )

    assert destination.exists()

    assert not source.exists()

    assert destination.read_text() == "Project Helios"
