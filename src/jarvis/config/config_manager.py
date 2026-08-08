import tomllib
from pathlib import Path


class ConfigManager:
    def load(self, filename: str) -> dict:
        config_path = Path(__file__).parent / filename

        with open(config_path, "rb") as file:
            return tomllib.load(file)
