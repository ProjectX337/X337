from core.memory.memory_manager import MemoryManager


memory = MemoryManager()


memory.remember(
    "test",
    "X337 memory online"
)


print(
    memory.recall(
        "test"
    )
)
