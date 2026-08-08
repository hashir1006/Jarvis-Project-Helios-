import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.search_engine import SearchEngine


def test_rank():

    engine = SearchEngine()

    results = engine.rank(
        "code",
        [
            "Chrome",
            "Movie Codec Installer",
            "CodeBlocks",
            "Visual Studio Code",
        ],
    )

    print()

    for name, score in results:
        print(name, score)

    assert results[0][0] == "Visual Studio Code"
