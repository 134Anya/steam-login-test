from browser.browser import Browser
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from .base_page import BasePage


class DynamicContentPage(BasePage):
    IMG_LOC = "(//*[contains(@class, 'large-2')])[{}]"
    ENDPOINT = "dynamic_content"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Dynamic Content"
        self.img = WebElement(self.browser, self.IMG_LOC.format(1), "Изображение")
        self.unique_element = WebElement(self.browser, self.IMG_LOC.format(1), "Первое изображение")

    def open(self):
        self.browser.open_endpoint(self.ENDPOINT)

    def get_img_src(self) -> list[str]:
        images = MultiWebElement(self.browser, self.IMG_LOC, "Список картинок")
        src_list = []
        for img in images:
            src_list.append(img.get_attribute("src"))
        return src_list
