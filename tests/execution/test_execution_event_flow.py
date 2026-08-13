from core.execution.coordinator import ExecutionCoordinator
from core.execution.bootstrap.default_capabilities import (
    create_default_router,
)
from core.execution.context.execution_context import ExecutionContext
from core.execution.events.event_bus import ExecutionEventBus
from core.graph.change_plan import ChangePlan, ChangeRequest
from core.graph.change import ChangeType


def test_execution_emits_runtime_events():

    bus = ExecutionEventBus()

    context = ExecutionContext(
        event_bus=bus
    )

    plan = ChangePlan(
        change=ChangeRequest(
            target_node="feature.auth",
            change_type=ChangeType.ADD,
        )
    )

    coordinator = ExecutionCoordinator(
        router=create_default_router()
    )

    coordinator.execute(
        plan,
        context=context,
    )

    events = [
        event.event_type
        for event in bus.all()
    ]

    assert "execution_started" in events
    assert "execution_completed" in events
