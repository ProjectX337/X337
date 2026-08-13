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

        failure_rate = analysis.get(
            "failure_rate",
            0.0,
        )

        success_rate = analysis.get(
            "success_rate",
            1.0,
        )

        if (
            failure_rate > 0.5
            or success_rate < 1.0
        ):
            signals.append(
                EngineeringSignal(
                    signal_type=SignalType.RUN_TESTS,
                    target_node="execution_runtime",
                    metadata={
                        "reason": (
                            "execution reliability "
                            "requires investigation"
                        ),
                        "failure_rate": failure_rate,
                        "success_rate": success_rate,
                    },
                )
            )

        return signals
