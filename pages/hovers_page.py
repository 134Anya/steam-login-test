from selenium.webdriver.common.by import By

from browser.browser import Browser
from core.config import Config
from elements.web_element import WebElement
from .base_page import BasePage


class HoverPage(BasePage):
    ENDPOINT = "hovers"
    UNIQUE_ELEMENT_LOC = (By.XPATH, '//*[contains(@class, "figure")]')

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Hovers"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC)

    def open(self):
        url = f"http://{Config.BASE_URL}/{self.ENDPOINT}"
        self.browser.get(url)

    def get_user_avatar(self, index: int) -> WebElement:
        user = (By.XPATH, f"(//*[contains(@class, 'figure')])[{index}]")
        return WebElement(self.browser, user)

    def get_user_name(self, index: int) -> WebElement:
        loc = (By.XPATH, f"//*[contains(@class, 'figure')][{index}]//h5")
        return WebElement(self.browser, loc)

    def get_user_link(self, index: int) -> WebElement:
        loc = (By.XPATH, f"(//div[@class='figure'])[{index}]//a")
        return WebElement(self.browser, loc)

    def hover_over_user(self, index: int):
        self.get_user_avatar(index).hover()

    def get_user_name_text(self, index: int) -> str:
        return self.get_user_name(index).get_text()

    def click_view_profile(self, index: int):
        self.get_user_link(index).click()