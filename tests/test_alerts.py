from faker import Faker

from data.test_data import TestData
from pages.javascript_alerts_page import JavascriptAlerts

fake = Faker()


class TestAlerts:

    def test_alerts(self, browser_fixture):
        page = JavascriptAlerts(browser_fixture)
        page.open()
        page.wait_for_open()

        page.js_click()
        alert_text = browser_fixture.get_alert_text()
        browser_fixture.accept_alert()
        assert TestData.ALERT_TEXT_EXPECTED == alert_text, \
            f"Текст алерта не совпал! Ожидали: {TestData.ALERT_TEXT_EXPECTED}, Получили: {alert_text}"
        page_result = page.get_result_text()
        assert TestData.RESULT_ALERT_SUCCESS == page_result, \
            f"Неверный алерт. Ожидался: {TestData.RESULT_ALERT_SUCCESS}, получен: {page_result} "

        page.js_confirm()
        alert_text = browser_fixture.get_alert_text()
        assert TestData.CONFIRM_TEXT_EXPECTED == alert_text, \
            f"Текст алерта не совпал. Ожидали : {TestData.CONFIRM_TEXT_EXPECTED}, Получили : {alert_text}"
        browser_fixture.accept_alert()
        page_result = page.get_result_text()
        assert TestData.RESULT_CONFIRM_OK == page_result, \
            f"Результат Confirm не совпал. Ожидали: {TestData.RESULT_CONFIRM_OK}, Получили: {page_result}"

        page.js_prompt()
        alert_text = browser_fixture.get_alert_text()
        assert TestData.PROMPT_TEXT_EXPECTED == alert_text
        random_text = fake.word()
        browser_fixture.send_keys_alert(random_text)
        browser_fixture.accept_alert()
        page_result = page.get_result_text()
        expected_result = f"You entered: {random_text}"
        assert expected_result == page_result, \
            f"Результат Prompt не совпал. Ожидали: '{expected_result}', Получили: '{page_result}'"
