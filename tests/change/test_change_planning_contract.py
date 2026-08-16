from core.planner.project_planner import ProjectPlanner


def test_project_spec_contains_change_plans():

    spec = ProjectPlanner().plan(
        "Create an AI tutor application"
    )

    assert spec.application_graph is not None

    assert spec.graph_intelligence is not None

    assert spec.change_plans is not None
