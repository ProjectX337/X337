from __future__ import annotations

from core.execution.capability import (
    ExecutionCapability,
    ExecutionResult,
)


class UpdateRouteCapability(
    ExecutionCapability
):

    name = "update_route"

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
