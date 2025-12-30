from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.configreader import ConfigReader
from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_FIELD_LOC = (By.XPATH, '//form[@role="search"]')
    SEARCH_INPUT_LOC = (By.XPATH, '//input[@name="term"]')

    def __init__(self, driver):
        super().__init__(driver)

    def ensure_main_page_loaded(self):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(self.SEARCH_FIELD_LOC))

    def search_game(self, game_name):
        search_box = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(self.SEARCH_INPUT_LOC))
        search_box.click()
        search_box.send_keys(Keys.CONTROL + "a", Keys.BACK_SPACE)
        search_box.send_keys(game_name, Keys.ENTER)
