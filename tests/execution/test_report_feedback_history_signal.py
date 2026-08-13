from core.execution.report.report_feedback import (
    ReportFeedbackProcessor,
)

from core.graph.signals import SignalType


def test_feedback_processor_uses_history_failure_rate():

    processor = ReportFeedbackProcessor()

    signals = processor.process(
        {
            "total_entries": 10,
            "failed_entries": 8,
            "failure_rate": 0.8,
        }
    )

    assert len(signals) == 1
    assert (
        signals[0].signal_type
        == SignalType.RUN_TESTS
    )
