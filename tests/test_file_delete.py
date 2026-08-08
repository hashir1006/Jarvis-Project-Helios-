import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.file_operations import FileOperations


def test_delete(tmp_path):

    operations = FileOperations()

    file = tmp_path / "delete_me.txt"

    file.write_text("Project Helios")

    assert file.exists()

    assert operations.delete(file)

    assert not file.exists()
