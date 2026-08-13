from core.execution.bootstrap.default_capabilities import (
    create_default_router,
)

from core.execution.coordinator import (
    ExecutionCoordinator,
)

from core.graph.change import (
    ChangeRequest,
    ChangeType,
)

from core.graph.change_plan import (
    ChangePlan,
)

from core.graph.signals import (
    EngineeringSignal,
    SignalType,
)


def test_execution_coordinator_runs_plan():

    router = create_default_router()

    coordinator = ExecutionCoordinator(
        router
    )

    plan = ChangePlan(
        change=ChangeRequest(
            target_node="feature.authentication",
            change_type=ChangeType.ADD,
        )
    )

    plan.add_signal(
        EngineeringSignal(
            signal_type=SignalType.MODIFY_COMPONENT,
            target_node="component.authform",
        )
    )

    report = coordinator.execute(
        plan
    )

    assert report.success is True
    assert len(report.results) == 1
    assert (
        report.results[0]
        .output["action"]
        == "modify_component"
    )
