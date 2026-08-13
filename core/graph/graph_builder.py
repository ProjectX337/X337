from __future__ import annotations

from core.graph.application_graph import ApplicationGraph
from core.graph.nodes import (
    FeatureNode,
    PageNode,
    ComponentNode,
)
from core.graph.edges import (
    GraphEdge,
    EdgeType,
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
                    FeatureNode(
                        id=feature_id,
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

            page_node = PageNode(
                id=page_id,
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
                                edge_type=(
                                    EdgeType.IMPLEMENTS
                                ),
                            )
                        )

            for component in page.components:

                component_id = (
                    f"component."
                    f"{component.name.lower().replace(' ', '_')}"
                )

                component_node = ComponentNode(
                    id=component_id,
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
                        edge_type=EdgeType.RENDERS,
                    )
                )

        return graph
