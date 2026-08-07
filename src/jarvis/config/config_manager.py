from pathlib import Path
import tomllib


class ConfigManager:
    def load(self, filename: str) -> dict:
        config_path = Path(__file__).parent / filename

        with open(config_path, "rb") as file:
            return tomllib.load(file)
            