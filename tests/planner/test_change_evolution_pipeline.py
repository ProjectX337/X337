from core.planner.project_planner import ProjectPlanner


def test_change_evolution_pipeline():

    planner = ProjectPlanner()

    spec = planner.plan(
        "Create an authentication dashboard application"
    )

    assert spec is not None
