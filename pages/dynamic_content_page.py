from selenium.webdriver.common.by import By

from browser.browser import Browser
from core.config import Config
from elements.web_element import WebElement
from .base_page import BasePage

class DynamicContentPage(BasePage):
    IMG_LOC = (By.XPATH, "//*[contains(@class, 'large-2')]")
    ENDPOINT = "dynamic_content"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Dynamic Content"
        self.img = WebElement(self.browser, self.IMG_LOC,"Изображение")
        self.unique_element = self.img

    def open(self):
        url = f"http://{Config.BASE_URL}/{self.ENDPOINT}"
        self.browser.get(url)

    def get_img_src(self) -> list[str]:
        image_elements = self.browser.find_elements(self.IMG_LOC)
        src_list = []
        for img in image_elements:
            src_list.append(img.get_attribute("src"))
        return src_list

    def refresh(self):
        self.browser.refresh()
        self.wait_for_open()