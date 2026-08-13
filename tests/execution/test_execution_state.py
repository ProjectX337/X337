from core.execution.execution_state import ExecutionState
from core.execution.capability import ExecutionResult


def test_execution_state_records_results():

    state = ExecutionState()

    state.record(
        ExecutionResult(
            success=True,
            output="done",
        )
    )

    assert len(state.results) == 1
    assert state.success is True
