from core.execution.report.report_analyzer import (
    ExecutionReportAnalyzer,
)

from core.execution.report.execution_report import (
    ExecutionReport,
)


def test_execution_report_analyzer():

    analyzer = ExecutionReportAnalyzer()

    reports = [
        ExecutionReport(
            execution_id="1",
            plan="plan",
            result="success",
        )
    ]

    result = analyzer.analyze(
        reports
    )

    assert result["total_reports"] == 1
    assert result["successful_reports"] == 1
