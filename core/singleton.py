from selenium import webdriver

class DriverSingleton:
    _instance = None
    _driver = None

    def get_driver(self):
        if self._driver is None:
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self._driver = webdriver.Chrome(options=options)
        return self._driver

    def close_driver(self):
        if self._driver:
            self._driver.quit()
            self._driver = None
