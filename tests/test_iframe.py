from pages.iframe_page import IframePage


class TestIframe:
    def test_iframe(self, browser_fixture):
        page = IframePage(browser_fixture)
        page.open()
        page.wait_for_open()
        page.navigate_to_nested_frames()

        browser_fixture.switch_to_frame(page.frame_top)
        assert page.get_frame_text() == "Parent frame", "Текст в Parent frame не совпадает"
        browser_fixture.switch_to_frame(page.frame_child)
        assert page.get_frame_text() == "Child Iframe", "Текст в Child frame не совпадает"

        browser_fixture.switch_to_default_content()
        page.navigate_to_frames()

        browser_fixture.switch_to_frame(page.frame_top)
        text_upper = page.get_frame_text()

        browser_fixture.switch_to_default_content()

        browser_fixture.switch_to_frame(page.frame_bottom)
        text_lower = page.get_frame_text()

        browser_fixture.switch_to_default_content()

        assert text_upper == text_lower, \
            f"Тексты не совпадают! Верхний: '{text_upper}', Нижний: '{text_lower}'"