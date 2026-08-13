from core.planner.planner import Planner


def test_project_spec_contains_product_intelligence():

    spec = Planner().plan(
        "Create an AI tutor application"
    )

    assert spec.product_spec is not None

    assert (
        spec.product_understanding
        is not None
    )

    assert (
        spec.application_graph
        is not None
    )