from core.planner.project_planner import ProjectPlanner


def test_project_spec_carries_ui_spec():

    planner = ProjectPlanner()

    spec = planner.plan(
        "Build an AI SaaS"
    )

    assert spec.ui_spec is not None

    assert isinstance(
        spec.ui_spec.pages,
        list,
    )

    assert isinstance(
        spec.ui_spec.components,
        list,
    )
