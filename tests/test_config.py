from jarvis.config.config_manager import ConfigManager


def test_voice_config():
    config = ConfigManager().load("voice.toml")

    assert config["tts"]["engine"] == "piper"
    assert config["stt"]["model"] == "base"
