from core.planner.project_planner import ProjectPlanner


def test_change_plan_execution_order_is_semantic():

    planner = ProjectPlanner()

    state = planner.plan_with_state(
        "Create an authentication dashboard application"
    )

    plan = state.change_plans[0]

    assert "modify_components" in plan.execution_order
    assert "run_tests" in plan.execution_order
