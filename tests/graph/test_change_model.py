from core.graph.change import (
    ChangeType,
    ChangeRequest,
    ChangePlan,
)


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


def test_change_plan_collection():

    plan = ChangePlan()

    plan.add(
        ChangeRequest(
            target_node="page.login",
            change_type=ChangeType.MODIFY,
        )
    )

    assert plan.count == 1

    assert (
        plan.changes[0].target_node
        == "page.login"
    )
