from __future__ import annotations

from pathlib import Path

from faster_whisper import WhisperModel


class SpeechToText:

    def __init__(self):
        print("[STT] Loading Whisper Model...")

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

        print("[STT] Model Ready")

    def transcribe(self, audio_path: Path) -> str:

        segments, _ = self.model.transcribe(str(audio_path))

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()