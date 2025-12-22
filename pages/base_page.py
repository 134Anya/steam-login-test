from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

class BasePage:
    def __init__(self, driver, url = None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def element_is_invisible(self, locator, timeout = 10):
        return wait(self.driver, timeout=timeout).until((EC.invisibility_of_element_located(locator)))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))

    def find_all(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def wait_for_unique_loc(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_staleness(self, element, timeout=10):
        wait(self.driver, timeout).until(EC.staleness_of(element))


