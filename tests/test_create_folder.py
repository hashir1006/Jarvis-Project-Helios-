import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.file_operations import FileOperations


def test_create_folder(tmp_path):

    operations = FileOperations()

    folder = tmp_path / "Helios"

    assert operations.create_folder(folder)

    assert folder.exists()

    assert folder.is_dir()
