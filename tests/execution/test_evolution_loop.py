from core.execution.evolution.evolution_loop import (
    EvolutionLoop,
)

from core.execution.signals.execution_signal import (
    ExecutionSignal,
)


def test_evolution_loop_creates_plan():

    loop = EvolutionLoop()

    result = loop.process(
        ExecutionSignal(
            signal_type="unstable_capability",
            action="apply_feature_change",
            target="runtime",
            severity=0.9,
        )
    )

    assert result is not None
    assert (
        result.change.target_node
        == "apply_feature_change"
    )
