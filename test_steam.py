import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import uuid



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login(driver):
    wait = WebDriverWait(driver, 10)


    login_page_loc = (By.CLASS_NAME, "global_action_link")
    username_loc = (By.XPATH, '//div[text()="Войдите, используя имя аккаунта"]/following::input[@type="text"][1]')
    password_loc = (By.XPATH, '//input[@type="password"]')
    login_button_loc = (By.XPATH, '//button[@type="submit" and contains(text(), "Войти")]')
    loading_indicator_loc = (By.XPATH, '//button[contains(text(), "Войти") and @disabled]')
    error_message_loc = (By.XPATH, "//div[contains(., 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.')]")

    driver.get("https://store.steampowered.com/")
    login_page = wait.until(EC.element_to_be_clickable(login_page_loc))
    login_page.click()

    username = wait.until(EC.visibility_of_element_located(username_loc))
    password = wait.until(EC.visibility_of_element_located(password_loc))


    wait.until(EC.element_to_be_clickable(login_button_loc))
    username.send_keys(str(uuid.uuid4))
    password.send_keys(str(uuid.uuid4))
    login_button = wait.until(EC.element_to_be_clickable(login_button_loc))
    login_button.click()
    wait.until(EC.presence_of_element_located(loading_indicator_loc))

    wait.until(EC.visibility_of_element_located(error_message_loc))
    error_element = driver.find_element(*error_message_loc)
    assert "Пожалуйста, проверьте свой пароль" in error_element.text


