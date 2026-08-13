from core.execution.report.report_history_analyzer import (
    ReportHistoryAnalyzer,
)

from core.execution.memory.execution_memory import (
    ExecutionMemoryEntry,
)


def test_report_history_analyzer_detects_failures():

    analyzer = ReportHistoryAnalyzer()

    result = analyzer.analyze(
        [
            ExecutionMemoryEntry(
                action="component",
                target="A",
                success=True,
            ),
            ExecutionMemoryEntry(
                action="component",
                target="A",
                success=False,
            ),
        ]
    )

    assert result["total_entries"] == 2
    assert result["failed_entries"] == 1
    assert result["failure_rate"] == 0.5
