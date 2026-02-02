from browser.browser import Browser
from elements.web_element import WebElement
from .base_page import BasePage


class BasicAuthPage(BasePage):
    CONGRATULATIONS_LOC = "//p[contains(text(), 'Congratulations')]"
    ENDPOINT = "basic_auth"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Basic Auth Page"
        self.congrats_label = WebElement(self.browser, self.CONGRATULATIONS_LOC, "Текст успешной авторизации")
        self.unique_element = WebElement(self.browser, self.CONGRATULATIONS_LOC, "Текст успешного входа")

    def login_with_credentials(self, username, password):
        self.browser.open_url_with_credentials(username, password, self.ENDPOINT)

    def is_congratulations_displayed(self):
        return self.congrats_label.is_exists()

    def get_congratulation_text(self) -> str:
        return self.congrats_label.get_text()