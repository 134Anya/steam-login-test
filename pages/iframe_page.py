from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from browser.browser import Browser
from elements.label import Label
from elements.web_element import WebElement
from elements.button import Button
from .base_page import BasePage


class IframePage(BasePage):
    NESTED_BTN_LOC = (By.XPATH, "//li[.//span[text()='Nested Frames']]")
    FRAMES_BTN_LOC = (By.XPATH, "//li[.//span[text()='Frames']]")
    FRAME_TOP_LOC = (By.ID, "frame1")

    FRAME_BOTTOM_LOC = (By.ID, "frame2")
    FRAME_CHILD_LOC = (By.TAG_NAME, "iframe")
    BODY_TEXT_LOC = (By.TAG_NAME, "body")
    WRAPPER_LOC = (By.ID, "framesWrapper")
    MAIN_HEADER_LOC = (By.CLASS_NAME, "main-header")

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Frames Page"
        self.nested_menu = Button(self.browser, self.NESTED_BTN_LOC, "Меню Nested")
        self.frames_menu = Button(self.browser, self.FRAMES_BTN_LOC, "Меню Frames")
        self.frames_wrapper = WebElement(self.browser, self.WRAPPER_LOC, "Контейнер фреймов")
        self.main_header = Label(self.browser, self.MAIN_HEADER_LOC, "Заголовок")
        self.unique_element = self.frames_wrapper
        self.frame_top = WebElement(self.browser, self.FRAME_TOP_LOC, "Верхний/Родительский фрейм")
        self.frame_child = WebElement(self.browser, self.FRAME_CHILD_LOC, "Вложенный фрейм")
        self.frame_bottom = WebElement(self.browser, self.FRAME_BOTTOM_LOC, "Нижний фрейм")
        self.content_text = Label(self.browser, self.BODY_TEXT_LOC, "Текст внутри фрейма")

    def open(self):
        self.browser.get("https://demoqa.com/")
        self.browser.get("https://demoqa.com/frames")

    def navigate_to_nested_frames(self):
        self.nested_menu.js_click()
        self.browser._wait.until(EC.url_contains("/nestedframes"))

    def navigate_to_frames(self):
        self.frames_menu.js_click()
        self.browser._wait.until(EC.url_to_be("https://demoqa.com/frames"))

    def get_header(self) -> str:
        return self.main_header.get_text()

    def get_frame_text(self) -> str:
        return self.content_text.get_text()