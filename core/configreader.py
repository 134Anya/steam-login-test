import json
import os


class ConfigReader:
    _config = None

    @staticmethod
    def get_config():
        if ConfigReader._config is None:
            root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            config_path = os.path.join(root_dir, "config.json")

            with open(config_path, "r", encoding="utf-8") as file:
                ConfigReader._config = json.load(file)

        return ConfigReader._config
