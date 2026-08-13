from core.execution.report.report_evolution_bridge import (
    ReportEvolutionBridge,
)


class FakeFeedback:
    def process(self, analysis):
        return ["signal"]


class FakeEvolution:
    def __init__(self):
        self.received = []

    def process(self, signal, context=None):
        self.received.append(
            (signal, context)
        )
        return "change-plan"


def test_runtime_report_evolution_pipeline():

    evolution = FakeEvolution()

    bridge = ReportEvolutionBridge(
        feedback_processor=FakeFeedback(),
        evolution_loop=evolution,
    )

    result = bridge.process(
        {
            "total_reports": 10,
            "success_rate": 0.5,
        },
        context={
            "execution": True,
        },
    )

    assert result == [
        "change-plan"
    ]

    assert evolution.received == [
        (
            "signal",
            {
                "execution": True,
            },
        )
    ]
