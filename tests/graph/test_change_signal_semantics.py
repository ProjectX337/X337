from core.planner.project_planner import ProjectPlanner
from core.graph.signals import SignalType


def test_change_plan_contains_semantic_signals():

    planner = ProjectPlanner()

    state = planner.plan_with_state(
        "Create an authentication dashboard application"
    )

    plan = state.change_plans[0]

    signal_types = [
        signal.signal_type
        for signal in plan.signals
    ]

    assert SignalType.MODIFY_COMPONENT in signal_types
    assert SignalType.RUN_TESTS in signal_types
