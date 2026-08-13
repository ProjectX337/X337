from __future__ import annotations

from core.graph.signals import (
    EngineeringSignal,
    SignalType,
)


class ReportFeedbackProcessor:
    """
    Converts execution analysis into engineering signals.

    Reporting does not mutate the application.
    It only produces evolution inputs.
    """

    def process(
        self,
        analysis: dict,
    ) -> list[EngineeringSignal]:

        signals = []

        success_rate = analysis.get(
            "success_rate",
            0.0,
        )

        if (
            analysis.get("total_reports", 0)
            and success_rate < 1.0
        ):
            signals.append(
                EngineeringSignal(
                    signal_type=SignalType.RUN_TESTS,
                    target_node="execution_runtime",
                    metadata={
                        "reason": (
                            "execution success rate "
                            "requires investigation"
                        ),
                        "success_rate": success_rate,
                    },
                )
            )

        return signals
