from pathlib import Path

from jarvis.voice.recorder import Recorder


def test_record():
    recorder = Recorder()

    output = recorder.record(
        seconds=5,
        output_path=Path("assets/audio/recordings/test.wav"),
    )

    assert output.exists()
