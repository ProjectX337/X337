from core.graph.models import ApplicationGraph
from core.graph.nodes import (
    FeatureNode,
    PageNode,
    ComponentNode,
)
from core.graph.edges import (
    GraphEdge,
    EdgeType,
)
from core.graph.query import GraphQuery


def build_graph():

    graph = ApplicationGraph()

    graph.add_node(
        FeatureNode(
            id="feature.auth",
            name="Authentication",
        )
    )

    graph.add_node(
        PageNode(
            id="page.login",
            name="Login",
        )
    )

    graph.add_node(
        ComponentNode(
            id="component.form",
            name="LoginForm",
        )
    )

    graph.add_edge(
        GraphEdge(
            source="feature.auth",
            target="page.login",
            edge_type=EdgeType.IMPLEMENTS,
        )
    )

    graph.add_edge(
        GraphEdge(
            source="page.login",
            target="component.form",
            edge_type=EdgeType.RENDERS,
        )
    )

    return graph


def test_feature_to_page_query():

    query = GraphQuery(build_graph())

    pages = query.find_pages_for_feature(
        "feature.auth"
    )

    assert pages[0].id == "page.login"


def test_page_to_component_query():

    query = GraphQuery(build_graph())

    components = query.find_components_for_page(
        "page.login"
    )

    assert components[0].id == "component.form"


def test_impact_surface_query():

    query = GraphQuery(build_graph())

    impacted = query.find_impact_surface(
        "feature.auth"
    )

    ids = {
        node.id
        for node in impacted
    }

    assert "page.login" in ids
    assert "component.form" in ids
