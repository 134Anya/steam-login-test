from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class ResultPage(BasePage):
    DROP_DOWN_LOC = (By.ID, "sort_by_trigger")
    SORT_OPTION_DESC_LOC = (By.ID, "Price_DESC")
    PRICE_LOC = (By.XPATH, '//*[contains(@class, "discount_final_price")]')
    LAST_RESULT_LOC = LAST_RESULT_IMAGE = (By.XPATH, '(//a[contains(@class, "search_result_row")])[last()]//img')
    RESULT_PAGE_LOADER_LOC = (By.XPATH, '//*[@id="search_result_container" and contains(@style, "opacity: 0.5")]')
    SEARCH_RESULT_ROW = (By.XPATH, "//*[@id='search_resultsRows']//a")

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_loaded(self):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(self.LAST_RESULT_LOC))

    def sort_by_price_desc(self):
        dropdown = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(self.DROP_DOWN_LOC))
        dropdown.click()

        option = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(self.SORT_OPTION_DESC_LOC))
        option.click()

        WebDriverWait(self.driver, self.timeout, poll_frequency=0.1).until(
            EC.visibility_of_element_located(self.RESULT_PAGE_LOADER_LOC))
        WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located(self.RESULT_PAGE_LOADER_LOC))
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(self.PRICE_LOC))

    def get_prices(self, n):
        elements = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(self.PRICE_LOC))
        prices = []

        for el in elements[:n]:
            text = el.text.strip()
            if "Free" in text or "Бесплатно" in text or not text:
                prices.append(0.0)
                continue
            clean_text = (text
                          .replace(" ", "")
                          .replace("руб", "")
                          .replace(",", ".")
                          )
            prices.append(float(clean_text))
        return prices
