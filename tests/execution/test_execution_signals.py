from core.execution.memory.execution_memory import (
    ExecutionMemory,
    ExecutionMemoryEntry,
)

from core.execution.signals.signal_generator import (
    ExecutionSignalGenerator,
)


def test_execution_signal_generation():

    memory = ExecutionMemory()

    memory.remember(
        ExecutionMemoryEntry(
            action="apply_feature_change",
            target="feature.auth",
            success=False,
        )
    )

    generator = ExecutionSignalGenerator()

    signal = generator.generate(
        memory,
        "apply_feature_change",
    )

    assert signal is not None
    assert signal.signal_type == (
        "unstable_capability"
    )
