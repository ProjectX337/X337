from core.graph.models import ApplicationGraph
from core.graph.models import (
    GraphNode,
    NodeKind,
)
from core.graph.models import (
    GraphEdge,
    EdgeRelation,
)
from core.graph.change import (
    ChangeRequest,
    ChangeType,
)
from core.graph.impact import (
    ImpactAnalyzer,
)


def test_feature_change_impact():

    graph = ApplicationGraph()

    feature = GraphNode(
        id="feature.auth",
        type=NodeKind.FEATURE,
        name="Authentication",
    )

    page = GraphNode(
        id="page.login",
        type=NodeKind.PAGE,
        name="Login",
    )

    graph.add_node(feature)
    graph.add_node(page)

    graph.add_edge(
        GraphEdge(
            source=feature.id,
            target=page.id,
            type=EdgeRelation.IMPLEMENTS,
        )
    )

    analyzer = ImpactAnalyzer(graph)

    report = analyzer.analyze(
        ChangeRequest(
            target_node="feature.auth",
            change_type=ChangeType.MODIFY,
        )
    )

    assert (
        report.changed_node
        == "feature.auth"
    )

    assert (
        "page.login"
        in report.affected_nodes
    )
