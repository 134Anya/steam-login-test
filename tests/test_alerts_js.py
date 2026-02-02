from faker import Faker

from data.test_data import TestData
from pages.javascript_alerts_page import JavascriptAlerts

fake = Faker()


class TestAlertsJs:
    def test_alerts_js(self, browser_fixture):
        page = JavascriptAlerts(browser_fixture)
        page.open()
        page.wait_for_open()

        page.trigger_js_alert()
        alert_text = browser_fixture.get_alert_text()
        assert TestData.ALERT_TEXT_EXPECTED == alert_text, f"Ожидался {TestData.ALERT_TEXT_EXPECTED},а получен {alert_text}"
        browser_fixture.accept_alert()
        assert TestData.RESULT_ALERT_SUCCESS == page.get_result_text(), f"Ожидался {TestData.RESULT_ALERT_SUCCESS}, а получен {page.get_result_text()}"

        page.trigger_js_confirm()
        alert_text = browser_fixture.get_alert_text()
        assert TestData.CONFIRM_TEXT_EXPECTED == alert_text, f"Ожидалось подтверждение {TestData.CONFIRM_TEXT_EXPECTED}, а получено {alert_text}"
        browser_fixture.accept_alert()
        assert TestData.RESULT_CONFIRM_OK == page.get_result_text(), f"Ожидалось {TestData.RESULT_CONFIRM_OK}, а получено {page.get_result_text()}"

        page.trigger_js_prompt()
        alert_text = browser_fixture.get_alert_text()
        assert TestData.PROMPT_TEXT_EXPECTED == alert_text, f"Ожидался {TestData.PROMPT_TEXT_EXPECTED}, а получен {alert_text}"
        random_text = fake.word()
        browser_fixture.send_keys_alert(random_text)
        browser_fixture.accept_alert()
        expected_result = f"You entered: {random_text}"
        assert expected_result == page.get_result_text(), f"Ожидался {expected_result}, получен {page.get_result_text()}"
