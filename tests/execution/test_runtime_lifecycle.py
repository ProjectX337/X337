from core.execution.lifecycle.runtime_lifecycle import (
    RuntimeLifecycle,
)


def test_runtime_lifecycle_contract():

    lifecycle = RuntimeLifecycle()

    assert lifecycle is not None
