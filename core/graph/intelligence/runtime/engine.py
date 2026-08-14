from __future__ import annotations

from core.graph.models import ApplicationGraph

from core.graph.intelligence.graph_reasoner import (
    GraphReasoner,
)

from core.graph.intelligence.architecture_analyzer import (
    ArchitectureAnalyzer,
)

from core.graph.intelligence.capability_mapper import (
    CapabilityMapper,
)


class GraphIntelligenceRuntime:
    """
    Coordinates intelligence analysis
    over the canonical ApplicationGraph.

    ApplicationGraph owns structure.
    Runtime derives intelligence.
    """

    def __init__(
        self,
        graph: ApplicationGraph,
    ):
        self.graph = graph

        self.reasoner = GraphReasoner()
        self.architecture = ArchitectureAnalyzer()
        self.capabilities = CapabilityMapper()


    def analyze(self):
        """
        Produce a complete graph intelligence report.
        """

        return {
            "reasoning": (
                self.reasoner.analyze(
                    self.graph
                )
            ),

            "architecture": (
                self.architecture.analyze(
                    self.graph
                )
            ),

            "graph": self.graph,

        }
