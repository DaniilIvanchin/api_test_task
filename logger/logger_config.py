import os
import logging

class LoggerConfig:
    LOGS_DIR_NAME = "logs"
    LOGS_FILE_NAME = LOGS_DIR_NAME + os.sep + "app.log"
    LOGGER_NAME = "TestLogger"
    LOGS_LEVEL = logging.INFO
    MAX_BYTES = 100_000
    BACKUP_COUNT = 10
    FORMAT = "[%(asctime)s] [%(levelname)s] - %(message)s"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"