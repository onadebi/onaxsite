import logging;
from datetime import datetime;

class LoggerService:
    def __init__(self):
        self._logger = logging.getLogger("onaxmain")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(f"onaxmain{datetime.now().date()}.log")
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)

    def log(self, message: str):
        """Logs the message to the log file"""
        print(str(message))
        self._logger.info(message)