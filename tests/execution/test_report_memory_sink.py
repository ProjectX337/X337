from core.execution.report.report_memory_sink import (
    ReportMemorySink,
)

from core.execution.memory.execution_memory import (
    ExecutionMemory,
)

from core.execution.report.execution_report import (
    ExecutionReport,
)


def test_report_memory_sink():

    memory = ExecutionMemory()

    sink = ReportMemorySink(
        memory=memory,
    )

    report = ExecutionReport(
        execution_id="exec-1",
        plan="plan",
        result="success",
    )

    result = sink.store(
        report
    )

    assert result.execution_id == "exec-1"
