from core.execution.bootstrap.runtime_factory import (
    create_execution_runtime,
)


def test_runtime_factory():

    runtime = create_execution_runtime()

    assert runtime is not None
