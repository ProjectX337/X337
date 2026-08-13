from core.execution.report.report_builder import (
    ExecutionReportBuilder,
)


def test_execution_report_builder():

    builder = ExecutionReportBuilder()

    report = builder.build(
        execution_id="exec-1",
        plan="plan",
        result="success",
    )

    assert report.execution_id == "exec-1"
    assert report.result == "success"
