from browser.browser import Browser
from elements.web_element import WebElement
from .base_page import BasePage


class JavascriptAlerts(BasePage):
    UNIQUE_ELEMENT_LOC = '//button[@onclick = "jsPrompt()"]'
    JS_ALERT_BUTTON_LOC = '//button[@onclick = "jsAlert()"]'
    JS_CONFIRM_BUTTON_LOC = '//button[@onclick = "jsConfirm()"]'
    JS_PROMPT_BUTTON_LOC = '//button[@onclick = "jsPrompt()"]'
    RESULT_TEXT_LOC = 'result'
    ENDPOINT = "javascript_alerts"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Javascript Alerts"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         "jsPrompt кнопка тут уникальный элемент")
        self.button_alert = WebElement(self.browser, self.JS_ALERT_BUTTON_LOC, "кнопка 'Click for JS Alert'")
        self.confirm_button = WebElement(self.browser, self.JS_CONFIRM_BUTTON_LOC, "кнопка 'Click for JS Confirm'")
        self.prompt_button = WebElement(self.browser, self.JS_PROMPT_BUTTON_LOC, "кнопка 'Click for JS Prompt'")
        self.result_text = WebElement(self.browser, self.RESULT_TEXT_LOC, "Текст результата")

    def open(self):
        self.browser.open_endpoint(self.ENDPOINT)

    def js_click(self):
        self.button_alert.wait_for_visible().click()

    def js_confirm(self):
        self.confirm_button.wait_for_visible().click()

    def js_prompt(self):
        self.prompt_button.wait_for_visible().click()

    def get_result_text(self):
        return self.result_text.get_text()

    def trigger_js_alert(self):
        self.browser.execute_script("jsAlert()")

    def trigger_js_prompt(self):
        self.browser.execute_script("jsPrompt()")

    def trigger_js_confirm(self):
        self.browser.execute_script("jsConfirm()")
