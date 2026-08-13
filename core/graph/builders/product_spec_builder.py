from __future__ import annotations

from core.intelligence.product_spec import ProductSpec
from core.graph.application_graph import (
    ApplicationGraph,
    GraphNode,
    GraphNodeType,
    GraphEdge,
    GraphEdgeType,
)


class ProductSpecGraphBuilder:
    """
    Converts product intelligence artifacts
    into executable application topology.
    """

    def build(
        self,
        spec: ProductSpec,
    ) -> ApplicationGraph:

        graph = ApplicationGraph()

        product_node = GraphNode(
            id="product",
            type=GraphNodeType.PRODUCT,
            name=spec.name,
            metadata={
                "product_type": spec.product_type,
            },
        )

        graph.add_node(product_node)

        for feature in spec.features:
            feature_node = GraphNode(
                id=f"feature.{feature.replace(' ', '_')}",
                type=GraphNodeType.FEATURE,
                name=feature,
            )

            graph.add_node(feature_node)

            graph.add_edge(
                GraphEdge(
                    source="product",
                    target=feature_node.id,
                    type=GraphEdgeType.REQUIRES,
                )
            )

        for entity in spec.entities:
            entity_node = GraphNode(
                id=f"entity.{entity.replace(' ', '_')}",
                type=GraphNodeType.ENTITY,
                name=entity,
            )

            graph.add_node(entity_node)

            graph.add_edge(
                GraphEdge(
                    source="product",
                    target=entity_node.id,
                    type=GraphEdgeType.REQUIRES,
                )
            )

        return graph
