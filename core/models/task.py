from core.memory.memory_manager import MemoryManager
from core.reflection.reflection_manager import ReflectionManager



class Task:


    def __init__(
        self,
        title
    ):


        self.title = title


        self.history = []


        self.context = {}


        self.memory = MemoryManager()


        self.reflection = ReflectionManager()