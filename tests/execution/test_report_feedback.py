from core.execution.report.report_feedback import (
    ReportFeedbackProcessor,
)

from core.graph.signals import (
    SignalType,
)


def test_report_feedback_generates_engineering_signal():

    processor = ReportFeedbackProcessor()

    signals = processor.process(
        {
            "total_reports": 10,
            "successful_reports": 5,
            "success_rate": 0.5,
        }
    )

    assert len(signals) == 1
    assert (
        signals[0].signal_type
        == SignalType.RUN_TESTS
    )
