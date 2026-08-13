from core.execution.mapping.signal_actions import (
    resolve_action,
)

from core.graph.signals import SignalType


def test_signal_type_maps_to_execution_action():

    assert (
        resolve_action(
            SignalType.MODIFY_COMPONENT
        )
        == "apply_feature_change"
    )


def test_unknown_signal_mapping_fails():

    class FakeSignal:
        pass

    try:
        resolve_action(FakeSignal())
        assert False
    except ValueError:
        assert True
