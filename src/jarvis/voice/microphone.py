import sounddevice as sd


class Microphone:
    def __init__(self):
        self.device = None

    def initialize(self):
        print("[Microphone] Initializing...")
        self.device = sd.default.device
        print("[Microphone] Ready")

    def list_devices(self):
        print("\nAvailable Audio Devices:\n")
        print(sd.query_devices())

    def device_info(self):
        if self.device is None:
            self.initialize()

        print(sd.query_devices(self.device[0]))