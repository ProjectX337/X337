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


def test_report_evolution_bridge_routes_signals():

    evolution = FakeEvolution()

    bridge = ReportEvolutionBridge(
        feedback_processor=FakeFeedback(),
        evolution_loop=evolution,
    )

    result = bridge.process(
        {
            "success_rate": 0.5,
        },
        context={"test": True},
    )

    assert result == [
        "change-plan"
    ]

    assert evolution.received == [
        (
            "signal",
            {"test": True},
        )
    ]
