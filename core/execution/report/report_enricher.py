from __future__ import annotations

from core.execution.report.execution_report import (
    ExecutionReport,
)


class ExecutionReportEnricher:
    """
    Adds execution intelligence data to reports.

    Responsibilities:
        - attach feedback
        - attach signals
        - attach evolution plans
        - attach lifecycle events
    """

    def enrich(
        self,
        report: ExecutionReport,
        feedback=None,
        signals=None,
        evolution_plan=None,
        events=None,
    ):

        report.feedback = feedback

        report.signals = (
            signals
            or report.signals
        )

        report.evolution_plan = (
            evolution_plan
            or report.evolution_plan
        )

        report.events = (
            events
            or report.events
        )

        return report
