from __future__ import annotations

from core.execution.memory.execution_memory import (
    ExecutionMemory,
    ExecutionMemoryEntry,
)


class ReportMemorySink:
    """
    Persists execution reports into execution memory.

    Execution flow:

        ExecutionReport
              |
              v
        ReportMemorySink
              |
              v
        ExecutionMemory
    """

    def __init__(
        self,
        memory: ExecutionMemory,
    ):
        self.memory = memory


    def store(
        self,
        report,
    ):

        self.memory.remember(
            ExecutionMemoryEntry(
                action=str(
                    report.plan
                ),
                target=str(
                    report.execution_id
                ),
                success=True,
            )
        )

        return report
