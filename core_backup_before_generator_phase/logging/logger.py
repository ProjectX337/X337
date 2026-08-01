from datetime import datetime
from pathlib import Path

from core.config.settings import Settings


class Logger:

    def __init__(self):

        Path(Settings.LOG_DIRECTORY).mkdir(
            exist_ok=True
        )

        self.log_file = (
            Path(Settings.LOG_DIRECTORY)
            / "x337.log"
        )

    def clear(self):

        with open(self.log_file, "w"):
            pass

    def write(self, message):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open(self.log_file, "a") as file:

            file.write(
                f"[{timestamp}] {message}\n"
            )