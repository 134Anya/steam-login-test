from selenium.webdriver.common.by import By

from browser.browser import Browser
from core.config import Config
from elements.web_element import WebElement
from .base_page import BasePage


class HandlersPage(BasePage):
    CLICK_HERE_LOC = (By.XPATH, "//a[contains(text(), 'Click Here')]")
    ENDPOINT = "windows"
    NEW_WINDOW_HEADER_LOC = (By.XPATH, "//h3[text()='New Window']")

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.click_here = WebElement(self.browser, self.CLICK_HERE_LOC, "ссылка новой вкладки")
        self.new_window_header = WebElement(self.browser, self.NEW_WINDOW_HEADER_LOC, "Заголовок New Window")
        self.unique_element = WebElement(self.browser, self.CLICK_HERE_LOC, "уникальный элемент страницы")

    def open(self):
        self.browser.open_endpoint(self.ENDPOINT)

    def click_new_window_link(self):
        self.click_here.click()

    def get_new_window_text(self) -> str:
        return self.new_window_header.get_text()