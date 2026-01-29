from pages.scroll_page import ScrollPage

class TestScroll:
    def test_infinite_scroll(self, browser_fixture):
        page = ScrollPage(browser_fixture)
        page.open()
        page.wait_for_open()
        age = 10

        actual_count = page.scroll_to_count(age)
        assert actual_count >= age, f"Абзацев меньше возраста! Возраст: {age}, Найдено: {actual_count}"