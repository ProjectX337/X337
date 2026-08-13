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
            output=task,
        )


def test_execution_capability_contract():

    capability = DummyCapability()

    result = capability.execute(
        "hello"
    )

    assert result.success is True
    assert result.output == "hello"
