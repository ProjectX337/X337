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
        self.signal_generator = SignalGenerator(graph)

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

        execution_phases = []

        signal_types = {
            signal.signal_type.value
            for signal in signals.signals
        }

        if "modify_component" in signal_types:
            execution_phases.append(
                "modify_components"
            )

        if "update_route" in signal_types:
            execution_phases.append(
                "update_routes"
            )

        if "update_api_contract" in signal_types:
            execution_phases.append(
                "update_api_contracts"
            )

        if "update_database" in signal_types:
            execution_phases.append(
                "update_database"
            )

        if "run_tests" in signal_types:
            execution_phases.append(
                "run_tests"
            )

        plan.execution_order.extend(
            execution_phases
        )

        plan.add_validation(
            "run_tests"
        )

        return plan
