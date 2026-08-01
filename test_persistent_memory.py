from core.memory.memory_manager import MemoryManager


memory = MemoryManager()


memory.remember(
    "x337_status",
    "persistent memory online"
)


new_memory = MemoryManager()


print(
    new_memory.recall(
        "x337_status"
    )
)
