from __future__ import annotations


class TextToSpeech:
    """Base interface for speech synthesis."""

    def initialize(self) -> None:
        raise NotImplementedError

    def speak(self, text: str) -> None:
        raise NotImplementedError
