from __future__ import annotations

from core.graph.models import (
    ApplicationGraph,
    EdgeRelation,
    GraphEdge,
    GraphNode,
    NodeKind,
)

from .decision_node import DecisionNode
from .evidence_node import EvidenceNode


class DecisionGraph:

    def __init__(self):
        self.graph = ApplicationGraph()

    def add_decision(self, decision: DecisionNode):
        self.graph.add_node(
            GraphNode(
                id=decision.id,
                kind=NodeKind.DECISION,
                name=decision.winner,
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
                kind=NodeKind.EVIDENCE,
                name=evidence.message,
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
                relation=EdgeRelation.SUPPORTS,
                metadata={
                    "weight": evidence.weight,
                },
            )
        )
