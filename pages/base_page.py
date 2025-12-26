from core.configreader import ConfigReader

class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.timeout = ConfigReader.get_config()["timeout"]

    def open(self):
        self.driver.get(self.url)
