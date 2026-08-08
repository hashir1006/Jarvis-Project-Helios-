import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.file_operations import FileOperations


def test_rename(tmp_path):

    operations = FileOperations()

    old = tmp_path / "old.txt"
    new = tmp_path / "new.txt"

    old.write_text("hello")

    assert operations.rename(old, new)

    assert new.exists()

    assert not old.exists()
