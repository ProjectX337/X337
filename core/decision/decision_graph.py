from __future__ import annotations

from core.graph.graph import Graph
from core.graph.node import GraphNode
from core.graph.edge import GraphEdge

from .decision_node import DecisionNode
from .evidence_node import EvidenceNode


class DecisionGraph:

    def __init__(self):

        self.graph = Graph()

    def add_decision(self, decision: DecisionNode):

        self.graph.add_node(
            GraphNode(
                id=decision.id,
                kind="decision",
                label=decision.winner,
                data={
                    "confidence": decision.confidence,
                    "type": decision.decision_type,
                },
            )
        )

    def add_evidence(
        self,
        decision_id: str,
        evidence: EvidenceNode,
    ):

        self.graph.add_node(
            GraphNode(
                id=evidence.id,
                kind="evidence",
                label=evidence.message,
                data={
                    "weight": evidence.weight,
                    "source": evidence.source,
                },
            )
        )

        self.graph.add_edge(
            GraphEdge(
                source=evidence.id,
                target=decision_id,
                relation="supports",
                weight=evidence.weight,
            )
        )
