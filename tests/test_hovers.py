from pages.hovers_page import HoverPage

class TestHovers:
    def test_hovers(self, browser_fixture):
        page = HoverPage(browser_fixture)
        page.open()
        page.wait_for_open()

        for i in range(1, 4):
            page.hover_over_user(i)
            name_text = page.get_user_name_text(i)
            expected_name = f"name: user{i}"
            assert name_text == expected_name, f"Ожидалось имя {expected_name}, а получено имя {name_text}"

            page.click_view_profile(i)

            current_url = browser_fixture.get_current_url()
            assert f"/users/{i}" in current_url, f"Неверный URL. Ожидалось наличие /users/{i},а открыт {current_url}"

            browser_fixture.back()
            page.get_user_avatar(i).wait_for_visible()