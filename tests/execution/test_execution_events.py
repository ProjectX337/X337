from core.execution.events.execution_event import (
    ExecutionEvent,
)


def test_execution_event_contract():

    event = ExecutionEvent(
        event_type="validation_failed",
        action="apply_feature_change",
        target="feature.auth",
        message="blocked",
    )

    assert event.event_type == "validation_failed"
    assert event.action == "apply_feature_change"
