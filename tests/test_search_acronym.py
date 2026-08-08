import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.system.search_engine import SearchEngine


def test_acronym():

    engine = SearchEngine()

    acronym = engine.acronym("Visual Studio Code")

    print(acronym)

    assert acronym == "vsc"
