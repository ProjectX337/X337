from core.execution.report.execution_report import (
    ExecutionReport,
)


def test_execution_report_contract():

    report = ExecutionReport(
        execution_id="test",
        plan="change_plan",
    )

    assert report.execution_id == "test"
    assert report.plan == "change_plan"
    assert report.signals == []
    assert report.events == []
