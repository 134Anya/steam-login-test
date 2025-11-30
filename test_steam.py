import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT = 10
MAIN_PAGE = "https://store.steampowered.com/"
LOGIN_PAGE_LOC = (By.XPATH, '//a[contains(@class, "global_action_link")]')
USERNAME_LOC = (By.XPATH, '//div[text()="Войдите, используя имя аккаунта"]/following::input[@type="text"][1]')
PASSWORD_LOC = (By.XPATH, '//input[@type="password"]')
LOGIN_BUTTON_LOC = (By.XPATH, '//div[@data-featuretarget="login"]//button[@type="submit"]')
LOADING_INDICATOR_LOC = (By.XPATH, '//div[@data-featuretarget="login"]//button[@type="submit" and @disabled]')
ERROR_MESSAGE_LOC = (By.XPATH, '//button[@type="submit"]/parent::div/following-sibling::div')
EXPECTED_TEXT = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
UNIQUE_LOGIN_PAGE_LOC = (By.XPATH, '//img[contains(@src, "blob:https://store.steampowered.com")]')

fake = Faker()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login(driver):
    wait = WebDriverWait(driver, TIMEOUT)

    driver.get(MAIN_PAGE)
    login_page = wait.until(EC.element_to_be_clickable(LOGIN_PAGE_LOC))
    login_page.click()

    username = wait.until(EC.visibility_of_element_located(USERNAME_LOC))
    password = wait.until(EC.visibility_of_element_located(PASSWORD_LOC))

    wait.until(EC.presence_of_element_located(UNIQUE_LOGIN_PAGE_LOC))
    username.send_keys(fake.user_name())
    password.send_keys(fake.password())
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_LOC))
    login_button.click()
    wait.until(EC.presence_of_element_located(LOADING_INDICATOR_LOC))
    wait.until(EC.invisibility_of_element_located(LOADING_INDICATOR_LOC))


    error_element = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE_LOC))

    actual_text = error_element.text
    assert EXPECTED_TEXT in actual_text, f"Ожидаемый текст ошибки : {EXPECTED_TEXT}! Фактический текст ошибки : {actual_text}"
