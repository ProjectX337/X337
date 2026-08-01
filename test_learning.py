from core.memory.memory_manager import MemoryManager

from core.learning.workflow_history import WorkflowHistory



memory = MemoryManager()



learning = WorkflowHistory(
    memory
)



learning.record(

    "Create Python calculator",

    [
        "coding",
        "testing",
        "review"
    ],

    True

)



print(

    learning.get_history()

)



print(

    learning.best_recent_workflow()

)