from core.execution.evolution.signal_router import (
    SignalRouter,
)

from core.execution.signals.execution_signal import (
    ExecutionSignal,
)


def test_signal_creates_change_plan():

    router = SignalRouter()

    plan = router.route(
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
