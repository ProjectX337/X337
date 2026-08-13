from core.graph.application_graph import (
    ApplicationGraph,
)

from core.graph.evolution.models import (
    GraphChangeSet,
)

from core.graph.evolution.impact_predictor import (
    ImpactPredictor,
)


def test_predict_added_surface():

    report = ImpactPredictor().predict(
        ApplicationGraph(),
        GraphChangeSet(
            added_nodes=[
                "component.mfa"
            ]
        ),
    )

    assert (
        "component.mfa"
        in report.affected_nodes
    )

    assert report.severity == "medium"
