from selenium.webdriver.common.by import By

from browser.browser import Browser
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from .base_page import BasePage


class HoverPage(BasePage):
    ENDPOINT = "hovers"
    UNIQUE_ELEMENT_LOC = (By.XPATH, '//*[contains(@class, "figure")]')
    FIGURE_TEMPLATE = "(//*[contains(@class, 'figure')])[{}]"
    NAME_TEMPLATE = "(//*[contains(@class, 'figure')])[{}]//h5"
    LINK_TEMPLATE = "(//div[@class='figure'])[{}]//a"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Hovers"
        self.unique_element = WebElement(self.browser, self.FIGURE_TEMPLATE.format(1),
                                         "маркер загруженной страницы Hovers")

    def open(self):
        self.browser.open_endpoint(self.ENDPOINT)

    def get_user_avatar(self, index: int) -> WebElement:
        return WebElement(self.browser, self.FIGURE_TEMPLATE.format(index), f"Аватар {index}")

    def get_user_name(self, index: int) -> WebElement:
        return WebElement(self.browser, self.NAME_TEMPLATE.format(index), f"Имя {index}")

    def get_user_link(self, index: int) -> WebElement:
        return WebElement(self.browser, self.LINK_TEMPLATE.format(index), f"Ссылка {index}")

    def get_all_avatars(self) -> MultiWebElement:
        return MultiWebElement(self.browser, self.FIGURE_TEMPLATE, "Все аватары")

    def hover_over_user(self, index: int):
        self.get_user_avatar(index).hover()

    def get_user_name_text(self, index: int) -> str:
        return self.get_user_name(index).get_text()

    def click_view_profile(self, index: int):
        self.get_user_link(index).click()
