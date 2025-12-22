from selenium.webdriver.common.by import By

class MainPageLocators:
    SEARCH_FIELD_LOC = (By.XPATH, '//form[@role="search"]')
    SUBMIT_BUTTON_LOC = (By.XPATH, '//button[@type = "submit"]')
    FOOTER_LOC = (By.XPATH, 'footer_logo')
    #FEATURED_RECOMMENDED_LOC = (By.XPATH, '//div[contains(@class,"screenshot")]')


