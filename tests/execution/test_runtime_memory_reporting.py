from core.execution.bootstrap.runtime_factory import (
    create_execution_runtime,
)


def test_runtime_has_report_memory_sink():

    runtime = create_execution_runtime()

    assert runtime.report_memory_sink is not None
