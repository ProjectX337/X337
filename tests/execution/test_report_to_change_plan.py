from core.execution.bootstrap.runtime_factory import (
    create_execution_runtime,
)

from core.graph.signals import (
    SignalType,
)


def test_report_feedback_creates_engineering_signal():

    runtime = create_execution_runtime()

    analysis = {
        "total_reports": 10,
        "successful_reports": 7,
        "success_rate": 0.7,
    }

    signals = runtime.report_feedback_processor.process(
        analysis
    )

    assert len(signals) == 1

    assert (
        signals[0].signal_type
        == SignalType.RUN_TESTS
    )

    assert (
        signals[0].target_node
        == "execution_runtime"
    )
