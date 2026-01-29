from browser.browser import Browser
from core.config import Config
from elements.web_element import WebElement
from logger.logger import Logger
from .base_page import BasePage


class BasicAuthPage(BasePage):
    CONGRATULATIONS_LOC = "//p[contains(text(), 'Congratulations')]"
    ENDPOINT = "basic_auth"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Basic Auth Page"
        self.unique_element = WebElement(self.browser, self.CONGRATULATIONS_LOC, description="Текст успешного входа")

    def open_with_credentials(self, username, password):
        Logger.info(f"{self.page_name}: Открываю страницу с логином '{username}'")
        target_url = f"http://{username}:{password}@{Config.BASE_URL}/{self.ENDPOINT}"
        self.browser.get(target_url)

    def is_congratulations_displayed(self):
        return self.unique_element.is_exists()

    def get_congratulation_text(self) -> str:
        return self.unique_element.get_text()