from core.graph.signals import (
    EngineeringSignal,
    EngineeringSignalSet,
    SignalType,
)


def test_engineering_signal_collection():

    signals = EngineeringSignalSet()

    signals.add(
        EngineeringSignal(
            signal_type=SignalType.MODIFY_COMPONENT,
            target_node="component.login_form",
        )
    )

    signals.add(
        EngineeringSignal(
            signal_type=SignalType.RUN_TESTS,
            target_node="feature.auth",
        )
    )

    assert signals.count == 2

    assert (
        signals.signals[0].signal_type
        == SignalType.MODIFY_COMPONENT
    )
