from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from browser.browser import Browser
from elements.web_element import WebElement
from .base_page import BasePage


class SliderPage(BasePage):
    SLIDER_LOC = '//*[@type="range"]'
    SLIDER_VALUE = "range"
    ENDPOINT = "horizontal_slider"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.page_name = "Horizontal Slider"
        self.slider = WebElement(self.browser, self.SLIDER_LOC, "Слайдер")
        self.slider_value = WebElement(self.browser, self.SLIDER_VALUE, "значение слайдера")
        self.unique_element = self.slider

    def open(self):
        self.browser.open_endpoint(self.ENDPOINT)

    def get_min_value(self) -> float:
        val = self.slider.get_attribute("min")
        return float(val) if val else 0.0

    def get_max_value(self) -> float:
        val = self.slider.get_attribute("max")
        return float(val) if val else 5.0

    def get_step_value(self) -> float:
        val = self.slider.get_attribute("step")
        return float(val) if val else 0.5

    def get_slider_value(self) -> float:
        text = self.slider_value.get_text()
        return float(text) if text else 0.0

    def set_slider_value(self, target_value: float):
        min_val = self.get_min_value()
        step_val = self.get_step_value()
        steps = int((target_value - min_val) / step_val)
        actions = ActionChains(self.browser.driver)
        self.slider.click()
        actions.send_keys(Keys.HOME).send_keys(Keys.ARROW_RIGHT * steps).perform()
