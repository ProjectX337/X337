from core.execution.action_router import ActionRouter
from core.execution.task import ExecutionTask
from core.execution.capability import (
    ExecutionCapability,
    ExecutionResult,
)


class DummyCapability(
    ExecutionCapability
):

    name = "dummy"

    def execute(
        self,
        task,
    ):

        return ExecutionResult(
            success=True,
            output=task.target,
        )


def test_router_executes_capability():

    router = ActionRouter()

    router.register(
        "modify_component",
        DummyCapability(),
    )

    task = ExecutionTask(
        action="modify_component",
        target="component.authform",
    )

    result = router.execute(
        task
    )

    assert result.success is True
    assert result.output == "component.authform"
