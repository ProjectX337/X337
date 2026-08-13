from core.graph.change_plan import (
    ChangePlan,
    PlanStatus,
)

from core.graph.change import (
    ChangeRequest,
    ChangeType,
)

from core.graph.signals import (
    EngineeringSignal,
    SignalType,
)


def test_change_plan_tracks_evolution_strategy():

    request = ChangeRequest(
        target_node="feature.auth",
        change_type=ChangeType.MODIFY,
    )

    plan = ChangePlan(
        change=request,
    )

    plan.add_affected_node(
        "page.login"
    )

    plan.add_signal(
        EngineeringSignal(
            signal_type=SignalType.MODIFY_COMPONENT,
            target_node="component.form",
        )
    )

    plan.add_validation(
        "run_tests"
    )

    assert plan.status == PlanStatus.CREATED

    assert plan.affected_count == 1

    assert plan.signal_count == 1

    assert (
        plan.validation_steps[0]
        == "run_tests"
    )
