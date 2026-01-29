import pytest
from pages.javascript_alerts_page import JavascriptAlerts
from data.test_data import TestData
from logger.logger import Logger
from faker import Faker

fake = Faker()

class TestAlertsJs:
    def test_alerts_js(self, browser_fixture):
        page = JavascriptAlerts(browser_fixture)
        page.open()
        page.wait_for_open()

        page.trigger_js_alert()
        alert_text = browser_fixture.get_alert_text()
        assert TestData.ALERT_TEXT_EXPECTED == alert_text
        browser_fixture.accept_alert()
        assert TestData.RESULT_ALERT_SUCCESS == page.get_result_text()

        page.trigger_js_confirm()
        alert_text = browser_fixture.get_alert_text()
        assert TestData.CONFIRM_TEXT_EXPECTED == alert_text
        browser_fixture.accept_alert()
        assert  TestData.RESULT_CONFIRM_OK == page.get_result_text()

        page.trigger_js_prompt()
        alert_text = browser_fixture.get_alert_text()
        assert TestData.PROMPT_TEXT_EXPECTED == alert_text
        random_text = fake.word()
        browser_fixture.send_keys_alert(random_text)
        browser_fixture.accept_alert()
        expected_result = f"You entered: {random_text}"
        assert expected_result == page.get_result_text()