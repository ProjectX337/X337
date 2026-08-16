from core.intelligence.application_graph_enricher import (
    ApplicationGraphEnricher,
)

from core.graph.models import (
    ApplicationGraph,
    GraphNode,
    NodeKind,
)


def test_application_graph_enrichment():

    graph = ApplicationGraph()

    graph.add_node(
        GraphNode(
            id="project:demo",
            kind=NodeKind.PROJECT,
            name="demo",
        )
    )

    understanding = {
        "project": "demo",

        "react": {
            "features": [
                "auth"
            ],

            "pages": [
                "login"
            ],

            "components": [
                "auth-form"
            ],
        },

        "files": [
            "src/features/auth/pages/login.tsx",
            "src/features/auth/components/auth-form.tsx",
        ],
    }


    result = ApplicationGraphEnricher().enrich(
        graph,
        understanding,
    )


    assert result.has_node(
        "feature:auth"
    )

    assert result.has_node(
        "page:login"
    )

    assert result.has_node(
        "component:auth-form"
    )
