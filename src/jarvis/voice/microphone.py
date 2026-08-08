import sounddevice as sd


class Microphone:
    def __init__(self):
        self.device = None

    def initialize(self):
        print("[Microphone] Initializing...")
        self.device = sd.default.device
        print("[Microphone] Ready")

    def list_devices(self) -> list:

        devices = list(sd.query_devices())

        print("\nAvailable Audio Devices:\n")

        for index, device in enumerate(devices):
            print(f"[{index}] {device['name']}")

        return devices

    def device_info(self):
        if self.device is None:
            self.initialize()

        print(sd.query_devices(self.device[0]))
