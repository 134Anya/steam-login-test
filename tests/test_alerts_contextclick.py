
from data.test_data import TestData
from pages.context_menu_page import ContextMenu


class TestContextClick:
    def test_right_click(self, browser_fixture):
        page = ContextMenu(browser_fixture)
        page.open()
        page.wait_for_open()

        page.right_click()
        alert_text = browser_fixture.get_alert_text()
        assert TestData.CONTEXT_MENU_SUCCESS_TEXT == alert_text
        browser_fixture.accept_alert()