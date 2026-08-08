from __future__ import annotations

from pathlib import Path

from jarvis.core.command_dispatcher import CommandDispatcher
from jarvis.core.intent_parser import IntentParser
from jarvis.voice.microphone import Microphone
from jarvis.voice.recorder import Recorder
from jarvis.voice.speech_to_text import SpeechToText


class VoicePipeline:

    def __init__(self):

        self.microphone = Microphone()
        self.recorder = Recorder()
        self.stt = SpeechToText()
        self.parser = IntentParser()
        self.dispatcher = CommandDispatcher()

        self.audio_path = Path("runtime/audio/input.wav")

    def listen(self):

        print("[Pipeline] Listening...")

    def record(self):

        return self.recorder.record(
            seconds=5,
            output_path=self.audio_path,
        )

    def transcribe(
        self,
        audio: Path,
    ) -> str:

        print("[Pipeline] Transcribing...")

        return self.stt.transcribe(audio)

    def understand(
        self,
        text: str,
    ):

        print("[Pipeline] Understanding...")

        return self.parser.parse(text)

    def execute(
        self,
        intent,
    ):

        print("[Pipeline] Executing...")

        return self.dispatcher.dispatch(intent)

    def run(self):

        self.listen()

        audio = self.record()

        text = self.transcribe(audio)

        print(f"[Pipeline] Recognized: {text}")

        intent = self.understand(text)

        if intent is None:
            print("[Pipeline] No intent recognized.")
            return None

        print(f"[Pipeline] Action : {intent.action}")
        print(f"[Pipeline] Target : {intent.target}")

        return self.execute(intent)