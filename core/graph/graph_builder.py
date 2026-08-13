from __future__ import annotations

from core.graph.models import ApplicationGraph
from core.graph.models import (
    GraphNode,
    GraphEdge,
    NodeKind,
    EdgeRelation,
)


class GraphBuilder:
    """
    Converts canonical UI models into an ApplicationGraph.

    The graph is a read-model of the application.
    It does not replace UISpec ownership.
    """

    def build(
        self,
        ui_spec,
        features=None,
    ) -> ApplicationGraph:

        graph = ApplicationGraph()

        if features:
            for feature in features:
                feature_id = (
                    f"feature."
                    f"{feature.slug}"
                )

                graph.add_node(
                    GraphNode(
                        id=feature_id,
                        kind=NodeKind.FEATURE,
                        name=feature.name,
                        metadata={
                            "description": (
                                feature.description
                            ),
                        },
                    )
                )

        for page in ui_spec.pages:

            page_id = (
                f"page."
                f"{page.name.lower().replace(' ', '_')}"
            )

            page_node = GraphNode(
                id=page_id,
                kind=NodeKind.PAGE,
                name=page.name,
                metadata={
                    "route": page.route,
                    "layout": page.layout,
                },
            )

            graph.add_node(page_node)

            if features:
                for feature in features:
                    if page.name in feature.pages:
                        graph.add_edge(
                            GraphEdge(
                                source=(
                                    f"feature."
                                    f"{feature.slug}"
                                ),
                                target=page_id,
                                relation=EdgeRelation.IMPLEMENTS,
                            )
                        )

            for component in page.components:

                component_id = (
                    f"component."
                    f"{component.name.lower().replace(' ', '_')}"
                )

                component_node = GraphNode(
                    id=component_id,
                    kind=NodeKind.COMPONENT,
                    name=component.name,
                    metadata={
                        "type": (
                            component.component_type
                        ),
                    },
                )

                graph.add_node(component_node)

                graph.add_edge(
                    GraphEdge(
                        source=page_id,
                        target=component_id,
                        relation=EdgeRelation.RENDERS,
                    )
                )

        return graph
