import logging
import os


class LoggerConfig:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    LOGS_DIR_NAME = os.path.join(BASE_DIR, "logs")
    LOGGER_NAME = "Logger"
    if not os.path.exists(LOGS_DIR_NAME):
        os.makedirs(LOGS_DIR_NAME)
    LOGS_FILE_NAME = os.path.join(LOGS_DIR_NAME, "api.log")
    LOGS_LEVEL = logging.INFO
    MAX_BYTES = 100000
    BACKUP_COUNT = 10
    FORMAT = "[%(asctime)s - %(levelname)s] - %(message)s"
    DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
