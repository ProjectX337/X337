from core.execution.observability.execution_trace import (
    ExecutionTrace,
)

from core.execution.observability.execution_metrics import (
    ExecutionMetrics,
)


def test_execution_trace_records_events():

    trace = ExecutionTrace(
        action="apply_feature_change",
        target="feature.auth",
    )

    trace.add_event(
        "execution_started"
    )

    assert len(trace.events) == 1


def test_execution_metrics():

    metrics = ExecutionMetrics()

    class Result:
        success = True

    metrics.record(Result())

    assert metrics.total == 1
    assert metrics.success_rate == 1
