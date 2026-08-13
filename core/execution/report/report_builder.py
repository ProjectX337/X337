from __future__ import annotations

from core.execution.report.execution_report import (
    ExecutionReport,
)


class ExecutionReportBuilder:

    def build(
        self,
        execution_id: str,
        plan,
        result,
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
