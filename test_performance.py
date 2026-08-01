from core.memory.memory_manager import MemoryManager

from core.learning.performance_tracker import PerformanceTracker



memory = MemoryManager()


tracker = PerformanceTracker(

    memory

)



tracker.record(

    "Coder",

    True

)


tracker.record(

    "Coder",

    True

)


tracker.record(

    "Tester",

    False

)



print(

    tracker.leaderboard()

)