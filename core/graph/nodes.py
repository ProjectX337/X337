"""
Compatibility exports.

Canonical graph storage lives in core.graph.models.
This module preserves legacy node constructors.
"""

from core.graph.models import (
    GraphNode,
    NodeKind as NodeType,
)


class FeatureNode(GraphNode):
    def __init__(
        self,
        id: str,
        name: str,
        metadata: dict | None = None,
    ):
        super().__init__(
            id=id,
            kind=NodeType.FEATURE,
            name=name,
            metadata=metadata or {},
        )


class PageNode(GraphNode):
    def __init__(
        self,
        id: str,
        name: str,
        metadata: dict | None = None,
    ):
        super().__init__(
            id=id,
            kind=NodeType.PAGE,
            name=name,
            metadata=metadata or {},
        )


class ComponentNode(GraphNode):
    def __init__(
        self,
        id: str,
        name: str,
        metadata: dict | None = None,
    ):
        super().__init__(
            id=id,
            kind=NodeType.COMPONENT,
            name=name,
            metadata=metadata or {},
        )


__all__ = [
    "GraphNode",
    "NodeType",
    "FeatureNode",
    "PageNode",
    "ComponentNode",
]
