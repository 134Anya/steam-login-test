import pytest
from core.configreader import ConfigReader
from core.singleton import DriverSingleton
from pages.main_page import MainPage


@pytest.fixture(scope="function")
def driver():
    driver_instance = DriverSingleton.get_driver()
    yield driver_instance
    DriverSingleton.close_driver()

@pytest.fixture
def open_main_page(driver):
    url = ConfigReader.get_config()["steam_url"]
    driver.get(url)
    return MainPage(driver)