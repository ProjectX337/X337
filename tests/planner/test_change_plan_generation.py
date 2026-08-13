from core.planner.project_planner import ProjectPlanner


def test_change_plan_generation():

    planner = ProjectPlanner()

    state = planner.plan_with_state(
        "Create an authentication dashboard application"
    )

    assert len(state.change_plans) >= 0
