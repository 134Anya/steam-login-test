import json
import os


class ConfigReader:
    _config = None

    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CONFIG_PATH = os.path.join(ROOT_DIR, "config.json")

    @staticmethod
    def get_config():
        if ConfigReader._config is None:
            with open(ConfigReader.CONFIG_PATH, "r", encoding="utf-8") as file:
                ConfigReader._config = json.load(file)

        return ConfigReader._config
