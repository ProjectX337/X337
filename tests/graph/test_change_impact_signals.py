from core.planner.project_planner import ProjectPlanner
from core.graph.signals import SignalType


def test_change_plan_uses_affected_nodes():

    planner = ProjectPlanner()

    state = planner.plan_with_state(
        "Create an authentication dashboard application"
    )

    auth_plan = state.change_plans[0]

    targets = [
        signal.target_node
        for signal in auth_plan.signals
    ]

    assert len(targets) > 0
