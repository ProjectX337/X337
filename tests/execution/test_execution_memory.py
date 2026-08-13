from core.execution.memory.execution_memory import (
    ExecutionMemory,
    ExecutionMemoryEntry,
)


def test_execution_memory_records_history():

    memory = ExecutionMemory()

    memory.remember(
        ExecutionMemoryEntry(
            action="apply_feature_change",
            target="feature.auth",
            success=True,
        )
    )

    assert len(memory.history()) == 1


def test_execution_memory_success_rate():

    memory = ExecutionMemory()

    memory.remember(
        ExecutionMemoryEntry(
            action="apply_feature_change",
            target="feature.auth",
            success=True,
        )
    )

    memory.remember(
        ExecutionMemoryEntry(
            action="apply_feature_change",
            target="feature.auth",
            success=False,
        )
    )

    assert memory.success_rate(
        "apply_feature_change"
    ) == 0.5
