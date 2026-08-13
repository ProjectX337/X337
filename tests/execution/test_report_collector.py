from core.execution.report.report_collector import (
    ExecutionReportCollector,
)


def test_report_collector():

    collector = ExecutionReportCollector()

    report = collector.collect(
        execution_id="exec-1",
        plan="plan",
        result="success",
    )

    assert report.execution_id == "exec-1"
    assert report.result == "success"
