from pages.handlers_page import HandlersPage


class TestHandlers:
    def test_windows(self, browser_fixture):
        page = HandlersPage(browser_fixture)
        page.open()
        page.wait_for_open()
        page.click_new_window_link()
        browser_fixture.switch_to_new_window()

        actual_text = page.get_new_window_text()
        expected_text = "New Window"

        assert actual_text == expected_text, \
            f"Ожидался заголовок: '{expected_text}', а получен: '{actual_text}'"

        browser_fixture.switch_to_default_window()

        page.click_new_window_link()
        browser_fixture.switch_to_new_window()
        assert page.get_new_window_text() == "New Window", f"Ожидался текст нового окна 'New Window', открыто окно с текстом {page.get_new_window_text()}"

        browser_fixture.switch_to_default_window()
        handles = browser_fixture.get_window_handles()
        browser_fixture.switch_to_window_by_handle(handles[1])
        browser_fixture.close()
        browser_fixture.switch_to_new_window()
        browser_fixture.close()

        browser_fixture.switch_to_default_window()
