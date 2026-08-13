from __future__ import annotations

from core.execution.capability import (
    ExecutionCapability,
    ExecutionResult,
)


class ModifyComponentCapability(
    ExecutionCapability
):

    name = "modify_component"


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
