from core.execution.bootstrap.runtime_factory import (
    create_execution_runtime,
)


def test_runtime_report_pipeline():

    runtime = create_execution_runtime()

    assert runtime.report_collector is not None
