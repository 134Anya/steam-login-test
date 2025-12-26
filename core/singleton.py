from selenium import webdriver

from core.configreader import ConfigReader


class DriverSingleton:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            config = ConfigReader.get_config()

            options = webdriver.ChromeOptions()
            if config["browser_options"]["start_maximized"]:
                options.add_argument("--start-maximized")
            cls._driver = webdriver.Chrome(options=options)
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
