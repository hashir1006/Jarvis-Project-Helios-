from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from jarvis.core.pipeline import VoicePipeline


def test_pipeline():

    pipeline = VoicePipeline()

    assert pipeline is not None