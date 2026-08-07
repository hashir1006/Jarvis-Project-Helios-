from jarvis.voice.microphone import Microphone


def test_microphone():
    mic = Microphone()
    devices = mic.list_devices()

    assert mic is not None