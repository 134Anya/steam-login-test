from pages.dynamic_content_page import DynamicContentPage

class TestDynamicContent:
    def test_dynamic_content(self, browser_fixture):
        page = DynamicContentPage(browser_fixture)
        page.open()
        page.wait_for_open()

        max_retries = 20
        match_found = False

        for attempt in range(max_retries):
            images_src = page.get_img_src()
            if len(set(images_src))<len(images_src):
                print(f"Обнаружен дубликат")
                match_found = True
                break
            page.refresh()

        assert match_found,f"За {max_retries} попыток  не обнаружено дубликатов изображений"