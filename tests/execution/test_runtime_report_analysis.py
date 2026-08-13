from core.execution.bootstrap.runtime_factory import (
    create_execution_runtime,
)


def test_runtime_can_analyze_reports():

    runtime = create_execution_runtime()

    analysis = runtime.report_analyzer.analyze(
        runtime.report_memory_sink.memory.history()
    )

    assert analysis["total_reports"] == 0
    assert analysis["successful_reports"] == 0
