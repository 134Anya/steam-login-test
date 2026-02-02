from selenium.webdriver.common.by import By

from browser.browser import Browser
from core.config import Config
from elements.input import Input
from .base_page import BasePage
from elements.label import Label
from elements.button import Button


class UploadImagePage(BasePage):
    UPLOAD_BUTTON_LOC =  "file-upload"
    SUBMIT_BUTTON_LOC = "file-submit"
    FILE_NAME_LOC = "uploaded-files"
    RESULT_TEXT = "//h3[text()='File Uploaded!']"
    DRAG_DROP_UPLOAD = "drag-drop-upload"
    DRAG_DROP_FILENAME_LOC =  "//*[@id='drag-drop-upload']//span[@data-dz-name]"
    CHECKMARK_LOC = "//*[@id='drag-drop-upload']//span[text()='✔']"
    ENDPOINT = "upload"

    def __init__(self, browser:Browser):
        super().__init__(browser)
        self.page_name = "File Uploader"
        self.file_input = Input(self.browser, self.UPLOAD_BUTTON_LOC, "кнопка UPLOAD")
        self.submit_btn = Button(self.browser, self.SUBMIT_BUTTON_LOC, "кнопка SUBMIT")
        self.uploaded_file_label = Label(self.browser, self.FILE_NAME_LOC,"Имя загруженного файла")
        self.unique_element = self.submit_btn
        self.success_header = Label(self.browser, self.RESULT_TEXT)
        self.drag_drop_upload = Button(self.browser, self.DRAG_DROP_UPLOAD)
        self.drop_filename = Label(self.browser, self.DRAG_DROP_FILENAME_LOC)
        self.success_checkmark = Label(self.browser, self.CHECKMARK_LOC, "Галочка успеха")

    def open(self):
        self.browser.open_endpoint(self.ENDPOINT)

    def upload_file(self, file_path:str):
        self.file_input.send_keys(file_path)
        self.submit_btn.click()

    def get_result_text(self)-> str:
        return self.success_header.get_text()

    def get_filename(self)-> str:
        return self.uploaded_file_label.get_text().strip()

    def click_upload_area(self):
        self.drag_drop_upload.click()

    def get_filename_drag_drop(self)->str:
        return self.drop_filename.get_text().strip()

    def is_checkmark_visible(self)->bool:
        try:
            return self.success_checkmark.wait_for_visible(timeout=5).is_displayed()
        except Exception:
            return False