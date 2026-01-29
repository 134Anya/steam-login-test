from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.label import Label
from elements.web_element import WebElement


class NestedFramesPage(BasePage):
    _PARENT_FRAME = (By.ID, "frame1")
    _CHILD_FRAME = (By.XPATH, "//iframe[contains(@srcdoc, 'Child Iframe')]")

    _PARENT_TEXT = (By.XPATH, "//*[contains(text(), 'Parent frame')]")
    _CHILD_TEXT = (By.XPATH, "//*[contains(text(), 'Child Iframe')]")

    def get_parent_text(self):
        self.browser.switch_to_frame(WebElement(self.browser, self._PARENT_FRAME, "Parent Frame"))
        text = Label(self.browser, self._PARENT_TEXT, "Parent Text").get_text().strip()
        self.browser.switch_to_default_content()
        return text

    def get_child_text(self):
        self.browser.switch_to_frame(WebElement(self.browser, self._PARENT_FRAME, "Parent Frame"))
        self.browser.switch_to_frame(WebElement(self.browser, self._CHILD_FRAME, "Child Frame"))
        text = Label(self.browser, self._CHILD_TEXT, "Child Text").get_text().strip()
        self.browser.switch_to_default_content()
        return text