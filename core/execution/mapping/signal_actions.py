from __future__ import annotations

from core.graph.signals import SignalType


SIGNAL_ACTION_MAP = {

    SignalType.MODIFY_COMPONENT:
        "apply_feature_change",

    SignalType.UPDATE_ROUTE:
        "update_route",

    SignalType.UPDATE_API_CONTRACT:
        "apply_feature_change",

    SignalType.UPDATE_DATABASE:
        "apply_feature_change",

    SignalType.RUN_TESTS:
        "run_tests",
}


def resolve_action(
    signal_type: SignalType,
) -> str:

    action = SIGNAL_ACTION_MAP.get(
        signal_type
    )

    if action is None:
        raise ValueError(
            f"No execution action mapped for {signal_type}"
        )

    return action
