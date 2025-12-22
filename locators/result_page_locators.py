from selenium.webdriver.common.by import By

class ResultPageLocators:
    DROP_DOWN_LOC = (By.ID, "sort_by_trigger")
    SORT_OPTION_DESC_LOC = (By.ID, "Price_DESC")
    SORT_LOC = (By.ID, "sort_by_trigger")
    PRICE_LOC = (By.XPATH, '//div[contains(@class, "discount_final_price")]')
    LAST_RESULT_LOC = LAST_RESULT_IMAGE = (By.XPATH, '(//a[contains(@class, "search_result_row")])[last()]//img')
    RESULT_PAGE_LOADER_LOC = (By.XPATH, '//div[@id="search_results" and @style = "opacity: 0.5;"]')
    SEARCH_RESULT_ROW = (By.XPATH, "//*[@id='search_resultsRows']/a")




