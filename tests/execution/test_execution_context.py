from core.execution.context.execution_context import (
    ExecutionContext,
)


def test_execution_context_defaults():

    context = ExecutionContext()

    assert context.project is None
    assert context.change_plan is None
    assert context.application_graph is None
