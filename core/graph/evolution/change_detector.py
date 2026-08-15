from __future__ import annotations

from core.graph.models import ApplicationGraph
from core.graph.evolution.models import GraphChangeSet


class ChangeDetector:
    """
    Detects architectural differences
    between graph versions.
    """

    def detect(
        self,
        before: ApplicationGraph,
        after: ApplicationGraph,
    ) -> GraphChangeSet:

        before_nodes = {
            node.id
            for node in before.nodes.values()
        }

        after_nodes = {
            node.id
            for node in after.nodes.values()
        }

        before_edges = {
            (
                edge.source,
                edge.target,
                edge.relation.value,
            )
            for edge in before.edges
        }

        after_edges = {
            (
                edge.source,
                edge.target,
                edge.relation.value,
            )
            for edge in after.edges
        }

        return GraphChangeSet(
            added_nodes=list(
                after_nodes - before_nodes
            ),
            removed_nodes=list(
                before_nodes - after_nodes
            ),
            added_edges=[
                str(edge)
                for edge in (
                    after_edges - before_edges
                )
            ],
            removed_edges=[
                str(edge)
                for edge in (
                    before_edges - after_edges
                )
            ],
        )
