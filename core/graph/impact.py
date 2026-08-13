from __future__ import annotations

from dataclasses import dataclass, field

from core.graph.application_graph import ApplicationGraph
from core.graph.change import ChangeRequest


@dataclass
class ImpactReport:
    """
    Describes the affected application surface
    caused by a requested change.
    """

    changed_node: str

    affected_nodes: list[str] = field(
        default_factory=list
    )


class ImpactAnalyzer:
    """
    Maps ChangeRequests onto ApplicationGraph
    impact surfaces.
    """

    def __init__(
        self,
        graph: ApplicationGraph,
    ):
        self.graph = graph

    def analyze(
        self,
        change: ChangeRequest,
    ) -> ImpactReport:

        affected = []

        node = self.graph.get_node(
            change.target_node
        )

        if node is None:
            return ImpactReport(
                changed_node=change.target_node,
                affected_nodes=[],
            )

        for edge in self.graph.edges:

            if edge.source == node.id:

                target = self.graph.get_node(
                    edge.target
                )

                if target:
                    affected.append(
                        target.id
                    )

        return ImpactReport(
            changed_node=node.id,
            affected_nodes=affected,
        )
