from core.graph.normalization.page_normalizer import (
    PageNormalizer,
)

from core.graph.models import (
    GraphNode,
    NodeKind,
)

from core.graph.graph import Graph


def test_page_identity_is_normalized():

    graph = Graph()

    graph.add_node(
        GraphNode(
            id="page.login_page",
            kind=NodeKind.PAGE,
            name="Login Page",
        )
    )

    graph.add_node(
        GraphNode(
            id="page.signin",
            kind=NodeKind.PAGE,
            name="Signin",
        )
    )

    PageNormalizer().normalize(
        graph
    )

    pages = {
        node.id
        for node in graph.nodes.values()
        if node.kind == NodeKind.PAGE
    }

    assert "page.login" in pages
    assert "page.login_page" not in pages
    assert "page.signin" not in pages
