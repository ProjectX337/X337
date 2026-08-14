from core.graph.models import ApplicationGraph
from core.graph.nodes import (
    FeatureNode,
    PageNode,
)
from core.graph.edges import (
    GraphEdge,
    EdgeType,
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

    feature = FeatureNode(
        id="feature.auth",
        name="Authentication",
    )

    page = PageNode(
        id="page.login",
        name="Login",
    )

    graph.add_node(feature)
    graph.add_node(page)

    graph.add_edge(
        GraphEdge(
            source=feature.id,
            target=page.id,
            edge_type=EdgeType.IMPLEMENTS,
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
