import random
from pages.slider_page import SliderPage

class TestActions:
    def test_slider(self, browser_fixture):
        page = SliderPage(browser_fixture)
        page.open()
        page.wait_for_open()

        min_val = page.get_min_value()
        max_val = page.get_max_value()
        step_val = page.get_step_value()

        total_steps = int((max_val - min_val) / step_val)
        if total_steps > 1:
            random_step_count = random.randint(1, total_steps - 1)
        else:
            random_step_count = 1

        target_value = min_val + (random_step_count * step_val)
        page.set_slider_value(target_value)
        actual_value = page.get_slider_value()

        assert round(page.get_slider_value(), 1) == round(target_value, 1), \
            f"Ошибка слайдера! Ожидалось: {target_value}, но на экране: {actual_value}"