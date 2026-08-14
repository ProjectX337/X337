"""
Compatibility exports.

Canonical graph runtime lives in core.graph.models.
"""

from core.graph.models import (
    ApplicationGraph,
    GraphNode,
    GraphEdge,
    NodeKind,
    EdgeRelation,
)

GraphNodeType = NodeKind
GraphEdgeType = EdgeRelation

__all__ = [
    "ApplicationGraph",
    "GraphNode",
    "GraphEdge",
    "NodeKind",
    "EdgeRelation",
    "GraphNodeType",
    "GraphEdgeType",
]
