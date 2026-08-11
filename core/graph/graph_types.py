"""
Compatibility graph type exports.

NodeKind is the canonical node vocabulary.
GraphNodeType remains as a compatibility alias while
the planner migrates.
"""

from core.graph.models import NodeKind

GraphNodeType = NodeKind

__all__ = [
    "NodeKind",
    "GraphNodeType",
]
