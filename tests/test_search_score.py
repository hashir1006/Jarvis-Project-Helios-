import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.search_engine import SearchEngine


def test_score():

    engine = SearchEngine()

    exact = engine.score(
        "Visual Studio Code",
        "Visual Studio Code",
    )

    partial = engine.score(
        "code",
        "Visual Studio Code",
    )

    fuzzy = engine.score(
        "vs cod",
        "Visual Studio Code",
    )

    print()

    print("Exact :", exact)
    print("Partial:", partial)
    print("Fuzzy :", fuzzy)

    assert exact == 100
    assert partial >= 90
    assert fuzzy >= 50
