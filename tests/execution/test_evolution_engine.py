from core.execution.evolution.evolution_engine import (
    EvolutionEngine,
)
from core.execution.signals.execution_signal import (
    ExecutionSignal,
)


def test_evolution_engine_creates_plan():

    engine = EvolutionEngine()

    plan = engine.evolve(
        ExecutionSignal(
            signal_type="unstable_capability",
            action="apply_feature_change",
            target="runtime",
            severity=0.8,
        )
    )

    assert plan is not None
    assert (
        plan.change.target_node
        == "apply_feature_change"
    )
