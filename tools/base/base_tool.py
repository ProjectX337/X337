from abc import ABC, abstractmethod
from datetime import datetime


class BaseTool(ABC):

    def __init__(self, name: str):
        self.name = name
        self.created_at = datetime.now()

    def log(self, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [Tool: {self.name}] {message}")

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass