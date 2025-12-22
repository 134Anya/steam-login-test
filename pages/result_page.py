
from pages.base_page import BasePage
from locators.result_page_locators import ResultPageLocators

class ResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=None)

    def ensure_page_loaded(self):
        self.wait_for_unique_loc(ResultPageLocators.LAST_RESULT_LOC)

    def sort_by_price_desc(self):
        dropdown = self.element_is_clickable(ResultPageLocators.DROP_DOWN_LOC)
        dropdown.click()

        old_row = self.element_is_visible(ResultPageLocators.SEARCH_RESULT_ROW)

        option = self.element_is_clickable(ResultPageLocators.SORT_OPTION_DESC_LOC)
        option.click()

        self.wait_for_staleness(old_row)

        #self.element_is_visible(ResultPageLocators.RESULT_PAGE_LOADER_LOC)
        #self.element_is_invisible(ResultPageLocators.RESULT_PAGE_LOADER_LOC)

    def get_prices(self, n):
        elements = self.find_all(ResultPageLocators.PRICE_LOC)
        prices = []

        for el in elements[:n]:
            text = el.text.strip()
            if "Free" in text or "Бесплатно" in text or not text:
                prices.append(0.0)
                continue
            clean_text = (text
                          .replace(" ","")
                          .replace("руб", "")
                          .replace(",", ".")
                          )
            prices.append(float(clean_text))
        return prices




