from __future__ import annotations

from pathlib import Path

from jarvis.voice.pyttsx3_tts import Pyttsx3TTS
from jarvis.core.command_dispatcher import CommandDispatcher
from jarvis.core.intent_parser import IntentParser
from jarvis.voice.microphone import Microphone
from jarvis.voice.recorder import Recorder
from jarvis.voice.speech_to_text import SpeechToText


class VoicePipeline:

    def __init__(self):

        self.tts = Pyttsx3TTS()
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

        self.tts.speak("Helios is online.")

        while True:

            self.listen()

            audio = self.record()

            text = self.transcribe(audio)

            print(f"\nYou: {text}")

            # Skip empty recognition
            if not text.strip():
                self.tts.speak("I didn't hear anything.")
                continue

            text_lower = text.lower().strip()

            # -----------------------------
            # Exit Helios
            # -----------------------------

            exit_phrases = (
                "exit helios",
                "quit helios",
                "goodbye helios",
                "shutdown helios",
                "shut down helios",
                "leave helios",
                "bye helios",
                "exit jarvis",
                "quit jarvis",
                "goodbye jarvis",
                "shutdown jarvis",
                "shut down jarvis",
                "leave jarvis",
                "bye jarvis",
                "stop listening",
            )

            if any(
                phrase in text_lower
                for phrase in exit_phrases
            ):
                self.tts.speak("Goodbye.")
                break

            # -----------------------------
            # Understand command
            # -----------------------------

            intent = self.understand(text)

            if intent is None:
                self.tts.speak(
                    "Sorry, I didn't understand."
                )
                continue

            print(f"Action : {intent.action}")
            print(f"Target : {intent.target}")

            # -----------------------------
            # Execute command
            # -----------------------------

            result = self.execute(intent)

            print(
                f"[Pipeline] Result: "
                f"success={result.success}, "
                f"message={result.message}"
            )

            # -----------------------------
            # Speak result
            # -----------------------------

            print("[Pipeline] Speaking...")

            self.tts.speak(result.message)

            print("[Pipeline] Speech finished.")