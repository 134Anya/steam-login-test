import os

class TestData:
    ADMIN_LOGIN = "admin"
    ADMIN_PASSWORD = "admin"

    ALERT_TEXT_EXPECTED = "I am a JS Alert"
    CONFIRM_TEXT_EXPECTED = "I am a JS Confirm"
    PROMPT_TEXT_EXPECTED = "I am a JS prompt"
    RESULT_CONFIRM_OK = "You clicked: Ok"
    RESULT_ALERT_SUCCESS = "You successfully clicked an alert"

    CONTEXT_MENU_SUCCESS_TEXT = "You selected a context menu"

    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FILE_PATH = os.path.join(PROJECT_ROOT, "resources", "idk.jpg")



