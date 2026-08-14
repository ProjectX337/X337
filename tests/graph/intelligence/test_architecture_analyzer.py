from core.graph.models import (
    ApplicationGraph,
    GraphNode,
    NodeKind,
)

from core.graph.intelligence.architecture_analyzer import (
    ArchitectureAnalyzer,
)


def test_architecture_analyzer_detects_incomplete_feature():

    graph = ApplicationGraph()

    graph.add_node(
        GraphNode(
            id="feature.auth",
            type=NodeKind.FEATURE,
            name="authentication",
        )
    )

    report = ArchitectureAnalyzer().analyze(
        graph
    )

    assert (
        "incomplete-feature:feature.auth"
        in report.risks
    )
