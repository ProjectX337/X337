from core.execution.report.execution_report import (
    ExecutionReport,
)


def test_runtime_reporting_contract():

    report = ExecutionReport(
        execution_id="exec-runtime",
        plan="plan",
        result="success",
    )

    assert report.execution_id == "exec-runtime"
    assert report.result == "success"
