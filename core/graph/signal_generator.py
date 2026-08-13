from __future__ import annotations

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

    def generate(
        self,
        change: ChangeRequest,
        impact: ImpactReport,
    ) -> EngineeringSignalSet:

        signals = EngineeringSignalSet()

        signals.add(
            EngineeringSignal(
                signal_type=SignalType.MODIFY_COMPONENT,
                target_node=change.target_node,
            )
        )

        for node_id in impact.affected_nodes:

            if node_id.startswith("page."):

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
