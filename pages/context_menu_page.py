from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.web_element import WebElement
from browser.browser import Browser
from logger.logger import Logger
from core.config import Config

class ContextMenu(BasePage):
    ENDPOINT = "context_menu"
    CONTEX_MENU_LOC = (By.ID, "hot-spot")

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Context menu"

        self.context_menu = WebElement(self.browser, self.CONTEX_MENU_LOC, "Выделенная область")
        self.unique_element = self.context_menu

    def open(self):
        url = f"http://{Config.BASE_URL}/{self.ENDPOINT}"
        self.browser.get(url)

    def right_click(self):
        self.context_menu.right_click()