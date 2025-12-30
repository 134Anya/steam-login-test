from core.configreader import ConfigReader


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = ConfigReader.get_config()["timeout"]
