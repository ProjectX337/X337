from core.logging.logger import Logger


class EventLogger:

    def __init__(self):

        self.logger = Logger()

    def handle(self, event):

        message = (
            f"[{event.source}] "
            f"{event.type}"
        )

        self.logger.write(message)