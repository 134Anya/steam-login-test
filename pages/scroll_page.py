import time

from selenium.webdriver.common.by import By

from browser.browser import Browser
from core.config import Config
from elements.web_element import WebElement
from .base_page import BasePage
from elements.label import Label

class ScrollPage(BasePage):

    ENDPOINT = "infinite_scroll"
    PARAGRAPH_LOC = (By.CLASS_NAME, "jscroll-added")
    HEADER_LOC = (By.TAG_NAME, "h3")

    def __init__(self, browser:Browser):
        super().__init__(browser)
        self.page_name = "Infinite Scroll"
        self.paragraph = WebElement(self.browser, self.PARAGRAPH_LOC, "Абзац")
        self.unique_element = Label(self.browser, self.HEADER_LOC, "Заголовок страницы")

    def open(self):
        url = f"http://{Config.BASE_URL}/{self.ENDPOINT}"
        self.browser.get(url)

    def get_count(self) -> int:
        elements = self.browser.find_elements(self.PARAGRAPH_LOC)
        return len(elements)

    def scroll_to_count(self, target_count:int, timeout = 67):
        start_time = time.time()

        while True:
            current_count = self.get_count()

            if current_count >= target_count:
                return current_count
            if time.time() - start_time > timeout:
                raise TimeoutError(
                    f"Не удалось загрузить {target_count} элементов. Сейчас загружено {current_count} абзацев"
                )
            prev_count = current_count
            self.browser.scroll_to_bottom()
            time.sleep(1)