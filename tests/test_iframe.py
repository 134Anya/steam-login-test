from pages.iframe_page import IframePage


def test_iframe(browser_fixture):
    page = IframePage(browser_fixture)

    page.open()
    page.wait_for_open()

    page.click_nested_frames()
    parent_text = page.get_nested_parent_text()
    assert parent_text == "Parent frame", f"Ожидалось 'Parent frame', но получено '{parent_text}'"
    child_text = page.get_nested_child_text()
    assert child_text == "Child Iframe", f"Ожидалось 'Child Iframe', но получено '{child_text}'"
    page.click_regular_frames()

    text_upper = page.get_frame_text_by_id(page.FRAME_PARENT_ID)
    text_lower = page.get_frame_text_by_id(page.FRAME_BOTTOM_ID)
    assert text_upper == text_lower, (
        f"Тексты фреймов не совпали! "
        f"Верхний: '{text_upper}', Нижний: '{text_lower}'"
    )