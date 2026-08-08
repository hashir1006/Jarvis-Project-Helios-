import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.file_search import FileSearch


def test_file_search():

    search = FileSearch()

    results = search.search(
        Path.home(),
        "python",
    )

    print(f"\nFound {len(results)} files")

    assert isinstance(results, list)
