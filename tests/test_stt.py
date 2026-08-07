from pathlib import Path

from jarvis.voice.speech_to_text import SpeechToText


def test_stt():

    stt = SpeechToText()

    text = stt.transcribe(
        Path("assets/audio/recordings/test.wav")
    )

    print(text)

    assert isinstance(text, str)