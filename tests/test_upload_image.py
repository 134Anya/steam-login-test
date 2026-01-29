import os
import time

import pyautogui
import pyperclip
from data.test_data import TestData
from pages.upload_image_page import UploadImagePage


class TestUpload:
    def test_upload_file(self, browser_fixture):
        page = UploadImagePage(browser_fixture)
        page.open()
        page.wait_for_open()
        full_path = TestData.FILE_PATH
        page.upload_file(full_path)
        file_name = os.path.basename(TestData.FILE_PATH)
        assert page.get_result_text() == "File Uploaded!", f"Ожидался заголовок 'File Uploaded!', получен заголовок {page.get_result_text()}"
        assert page.get_filename()==file_name, f"Ожидался файл {file_name}, загружен файл {page.get_filename()}"

    def test_upload_dialog(self, browser_fixture):
        page = UploadImagePage(browser_fixture)
        page.open()
        page.wait_for_open()
        full_path = TestData.FILE_PATH

        file_name = os.path.basename(full_path)
        page.click_upload_area()
        time.sleep(2)
        pyperclip.copy(full_path)
        pyautogui.hotkey('ctrl','v')
        time.sleep(0.5)
        pyautogui.press('enter')
        actual_name = page.get_filename_drag_drop()
        assert actual_name == file_name, \
            f"Имя файла не совпадает! Ждали: {file_name}, получили: {actual_name}"
        assert page.check_checkmark_visibility(), "Галочка '✔' не появилась!"