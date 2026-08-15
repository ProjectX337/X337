from __future__ import annotations

from core.graph.models import NodeKind
from core.graph.signals import (
    EngineeringSignal,
    EngineeringSignalSet,
    SignalType,
)
from core.graph.change import ChangeRequest
from core.graph.impact import ImpactReport


class SignalGenerator:
    """
    Converts graph changes and impact analysis into
    engineering actions.

    This layer does not modify code.
    It produces engineering intent only.
    """

    def __init__(self, graph):
        self.graph = graph

    def _graph_node(self, node_id: str):
        return self.graph.get_node(node_id)

    def generate(
        self,
        change: ChangeRequest,
        impact: ImpactReport,
    ) -> EngineeringSignalSet:

        signals = EngineeringSignalSet()

        for node_id in impact.affected_nodes:

            node = self._graph_node(node_id)

            if node is None:
                continue

            if node.kind == NodeKind.COMPONENT:

                signals.add(
                    EngineeringSignal(
                        signal_type=SignalType.MODIFY_COMPONENT,
                        target_node=node_id,
                    )
                )

            elif node.kind == NodeKind.PAGE:

                signals.add(
                    EngineeringSignal(
                        signal_type=SignalType.UPDATE_ROUTE,
                        target_node=node_id,
                    )
                )

        signals.add(
            EngineeringSignal(
                signal_type=SignalType.RUN_TESTS,
                target_node=change.target_node,
            )
        )

        return signals
