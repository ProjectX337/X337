from __future__ import annotations

from core.graph.change import ChangeRequest
from core.graph.change_plan import ChangePlan
from core.graph.impact import ImpactAnalyzer
from core.graph.signal_generator import SignalGenerator


class ChangePlanner:
    """
    Converts graph changes into executable evolution plans.

    This layer coordinates reasoning only.
    It does not modify files or execute changes.
    """

    def __init__(self, graph):
        self.graph = graph
        self.impact_analyzer = ImpactAnalyzer(graph)
        self.signal_generator = SignalGenerator()

    def create_plan(
        self,
        change: ChangeRequest,
    ) -> ChangePlan:

        impact = self.impact_analyzer.analyze(
            change
        )

        signals = self.signal_generator.generate(
            change,
            impact,
        )

        plan = ChangePlan(
            change=change,
            affected_nodes=impact.affected_nodes,
            signals=signals.signals,
        )

        plan.execution_order.extend(
            [
                signal.target_node
                for signal in signals.signals
            ]
        )

        plan.add_validation(
            "run_tests"
        )

        return plan
