from __future__ import annotations

from core.execution.capability import (
    ExecutionCapability,
    ExecutionResult,
)


class RunTestsCapability(
    ExecutionCapability
):

    name = "run_tests"

    def execute(
        self,
        task,
    ) -> ExecutionResult:

        return ExecutionResult(
            success=True,
            output={
                "action": self.name,
                "target": task.target,
            },
        )
