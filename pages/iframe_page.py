from selenium.webdriver.common.by import By
from browser.browser import Browser
from elements.web_element import WebElement
from elements.button import Button
from .base_page import BasePage


class IframePage(BasePage):
    URL = "https://demoqa.com/frames"

    NESTED_MENU_XPATH = "//span[text()='Nested Frames']"
    FRAMES_MENU_XPATH = "//span[text()='Frames']"
    FRAME_PARENT_ID = "frame1"
    FRAME_BOTTOM_ID = "frame2"
    FRAME_CHILD_XPATH = "//iframe[@srcdoc]"
    SAMPLE_TEXT_ID = "sampleHeading"
    BODY_XPATH = "//body"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Iframe Page"
        self.unique_element = WebElement(self.browser, "framesWrapper", "Контейнер фреймов")

    def open(self):
        self.browser.get(self.URL)

    def click_nested_frames(self):
        Button(self.browser, self.NESTED_MENU_XPATH, "Меню Nested Frames").js_click()
        self.unique_element = WebElement(self.browser, self.FRAME_PARENT_ID)
        self.wait_for_open()

    def click_frames_menu(self):
        Button(self.browser, self.FRAMES_MENU_XPATH, "Меню Frames").js_click()
        self.unique_element = WebElement(self.browser, "framesWrapper")
        self.wait_for_open()

    def get_nested_parent_text(self) -> str:
        self.browser.switch_to_frame(WebElement(self.browser, self.FRAME_PARENT_ID))
        text = WebElement(self.browser, self.BODY_XPATH, "Body родителя").get_text()
        self.browser.switch_to_default_content()
        return text

    def get_nested_child_text(self) -> str:
        self.browser.switch_to_frame(WebElement(self.browser, self.FRAME_PARENT_ID))
        self.browser.switch_to_frame(WebElement(self.browser, self.FRAME_CHILD_XPATH, "Вложенный фрейм"))
        text = WebElement(self.browser, self.BODY_XPATH, "Body ребенка").get_text()
        self.browser.switch_to_default_content()
        return text

    def get_frame_text_by_id(self, frame_id: str) -> str:
        self.browser.switch_to_frame(WebElement(self.browser, frame_id))
        text = WebElement(self.browser, self.SAMPLE_TEXT_ID, "Заголовок в фрейме").get_text()
        self.browser.switch_to_default_content()
        return text

    def click_regular_frames(self):
        Button(self.browser, self.FRAMES_MENU_XPATH, "Меню Frames").js_click()
        self.unique_element = WebElement(self.browser, "framesWrapper")
        self.wait_for_open()