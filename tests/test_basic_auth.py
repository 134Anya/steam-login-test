import pytest
from pages.basic_auth_page import BasicAuthPage
from data.test_data import TestData

class TestBasicAuth:

    def test_login_success(self, browser_fixture):

        page = BasicAuthPage(browser_fixture)
        page.open_with_credentials(TestData.ADMIN_LOGIN, TestData.ADMIN_PASSWORD)
        page.wait_for_open()
        actual_text = page.get_congratulation_text()
        expected_text = "Congratulations! You must have the proper credentials."
        assert expected_text == actual_text, \
        f"Ожидался текст успешного входа {expected_text}, но получен текст {actual_text}"