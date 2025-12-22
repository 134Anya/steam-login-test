from selenium.webdriver.common.action_chains import ActionChains
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    URL = "https://store.steampowered.com/"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def wait_for_open_main_page(self):
        self.open()
        self.wait_for_unique_loc(MainPageLocators.SEARCH_FIELD_LOC)

    def search_game(self, game_name):
        search_box = self.element_is_visible(MainPageLocators.SEARCH_FIELD_LOC)
        actions = ActionChains(self.driver)

        (actions.move_to_element(search_box).click().pause(0.5).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).send_keys(game_name).pause(0.5).send_keys(Keys.ENTER).perform())