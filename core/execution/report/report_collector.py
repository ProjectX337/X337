from __future__ import annotations

from core.execution.report.execution_report import (
    ExecutionReport,
)


class ExecutionReportCollector:
    """
    Collects execution lifecycle data into
    a final execution intelligence report.
    """

    def collect(
        self,
        execution_id,
        plan,
        result=None,
        feedback=None,
        signals=None,
        evolution_plan=None,
        events=None,
    ):

        return ExecutionReport(
            execution_id=execution_id,
            plan=plan,
            result=result,
            feedback=feedback,
            signals=signals or [],
            evolution_plan=evolution_plan,
            events=events or [],
        )
