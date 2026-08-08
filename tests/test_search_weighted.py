import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.search_engine import SearchEngine


def test_weighted():

    engine = SearchEngine()

    assert (
        engine.score(
            "Visual Studio Code",
            "Visual Studio Code",
        )
        == 100
    )

    assert (
        engine.score(
            "code",
            "Visual Studio Code",
        )
        == 95
    )

    assert (
        engine.score(
            "studio",
            "Visual Studio Code",
        )
        == 95
    )

    assert (
        engine.score(
            "vsc",
            "Visual Studio Code",
        )
        == 85
    )

    assert (
        engine.score(
            "visualstudiocode",
            "Visual Studio Code",
        )
        == 80
    )
