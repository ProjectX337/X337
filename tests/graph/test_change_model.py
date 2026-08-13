from core.graph.change import (
    ChangeType,
    ChangeRequest,
)

from core.graph.change_plan import ChangePlan


def test_change_request_creation():

    change = ChangeRequest(
        target_node="feature.auth",
        change_type=ChangeType.MODIFY,
        description="Add OAuth support",
    )

    assert change.target_node == "feature.auth"

    assert (
        change.change_type
        == ChangeType.MODIFY
    )


def test_change_plan_creation():

    change = ChangeRequest(
        target_node="page.login",
        change_type=ChangeType.MODIFY,
    )

    plan = ChangePlan(
        change=change,
    )

    assert plan.change.target_node == "page.login"

    assert plan.status.value == "created"

    assert plan.signal_count == 0

    assert plan.affected_count == 0
