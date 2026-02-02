from browser.browser import Browser
from elements.web_element import WebElement
from .base_page import BasePage


class ContextMenu(BasePage):
    ENDPOINT = "context_menu"
    CONTEXT_MENU_LOC = "hot-spot"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Context menu"
        self.context_menu = WebElement(self.browser, self.CONTEXT_MENU_LOC, "Выделенная область")
        self.unique_element = WebElement(self.browser, self.CONTEXT_MENU_LOC, "Маркер контекстного меню")

    def open(self):
        self.browser.open_endpoint(self.ENDPOINT)

    def right_click(self):
        self.context_menu.right_click()
