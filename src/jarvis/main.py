from voice.voice_manager import VoiceManager


def main():
    print("=" * 50)
    print("JARVIS OS Starting...")
    print("=" * 50)

    voice = VoiceManager()
    voice.initialize()

    print("JARVIS Core Ready")


if __name__ == "__main__":
    main()
