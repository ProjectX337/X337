from core.execution.execution_planner import ExecutionPlanner
from core.execution.context.execution_context import ExecutionContext
from core.graph.change_plan import ChangePlan
from core.graph.change import ChangeRequest, ChangeType
from core.graph.signals import EngineeringSignal, SignalType


def test_context_attached_to_execution_task():

    plan = ChangePlan(
        change=ChangeRequest(
            target_node="feature.auth",
            change_type=ChangeType.ADD,
        )
    )

    plan.add_signal(
        EngineeringSignal(
            signal_type=SignalType.MODIFY_COMPONENT,
            target_node="component.auth",
        )
    )

    context = ExecutionContext()

    tasks = ExecutionPlanner().create_tasks(
        plan,
        context=context,
    )

    assert tasks[0].context is context
