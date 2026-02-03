import pytest
from browser.browser_factory import BrowserFactory
from browser.browser import Browser
from logger.logger import Logger


@pytest.fixture(scope="function")
def browser_fixture():
    driver = BrowserFactory.get_driver()
    browser_wrapper = Browser(driver)

    yield browser_wrapper
    browser_wrapper.quit()