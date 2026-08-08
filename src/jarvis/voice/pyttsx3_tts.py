from __future__ import annotations

import pyttsx3

from jarvis.voice.text_to_speech import TextToSpeech


class Pyttsx3TTS(TextToSpeech):

    def __init__(self):

        print("[TTS] Initializing...")

        self.rate = 175
        self.volume = 1.0

        print("[TTS] Ready")

    def initialize(self) -> None:
        pass

    def speak(
        self,
        text: str,
    ) -> None:

        if not text.strip():
            return

        print(f"[TTS] Speaking: {text}")

        engine = None

        try:

            engine = pyttsx3.init()

            engine.setProperty(
                "rate",
                self.rate,
            )

            engine.setProperty(
                "volume",
                self.volume,
            )

            engine.say(text)

            engine.runAndWait()

        except Exception as error:

            print(
                f"[TTS] Speech error: {error}"
            )

        finally:

            if engine is not None:

                try:
                    engine.stop()

                except Exception:
                    pass

        print("[TTS] Finished")