from __future__ import annotations

from core.execution.feedback.execution_feedback import (
    ExecutionFeedback,
)

from core.execution.memory.execution_memory import (
    ExecutionMemory,
    ExecutionMemoryEntry,
)


class FeedbackProcessor:
    """
    Converts execution feedback into runtime memory.

    Execution lifecycle:

        Capability Result
              |
              v
        ExecutionFeedback
              |
              v
        FeedbackProcessor
              |
              v
        ExecutionMemory
    """

    def __init__(
        self,
        memory: ExecutionMemory,
    ):
        self.memory = memory


    def process(
        self,
        feedback: ExecutionFeedback,
    ):

        self.memory.remember(
            ExecutionMemoryEntry(
                action=feedback.action,
                target=feedback.target,
                success=feedback.success,
            )
        )
