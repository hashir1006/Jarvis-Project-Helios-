from __future__ import annotations

from pathlib import Path

import sounddevice as sd
import soundfile as sf


class Recorder:
    def __init__(
        self,
        sample_rate: int = 16000,
        channels: int = 1,
    ):
        self.sample_rate = sample_rate
        self.channels = channels

    def record(self, seconds: int, output_path: Path) -> Path:
        print(f"[Recorder] Recording for {seconds} seconds...")

        audio = sd.rec(
            int(seconds * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="float32",
        )

        sd.wait()

        output_path.parent.mkdir(parents=True, exist_ok=True)

        sf.write(output_path, audio, self.sample_rate)

        print(f"[Recorder] Saved: {output_path}")

        return output_path
