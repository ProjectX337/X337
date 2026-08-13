from __future__ import annotations

from core.execution.evolution.adapters.engineering_signal_adapter import (
    EngineeringSignalAdapter,
)



class ReportEvolutionBridge:
    """
    Converts execution intelligence into evolution actions.

    Reporting creates signals.
    Evolution decides changes.
    """

    def __init__(
        self,
        feedback_processor,
        evolution_loop,
    ):
        self.feedback_processor = feedback_processor
        self.evolution_loop = evolution_loop
        self.signal_adapter = EngineeringSignalAdapter()

    def process(
        self,
        analysis,
        context=None,
    ):
        signals = self.feedback_processor.process(
            analysis
        )

        results = []

        for signal in signals:

            if hasattr(
                signal,
                "signal_type",
            ):
                signal = (
                    self.signal_adapter.convert(
                        signal
                    )
                )

            results.append(
                self.evolution_loop.process(
                    signal,
                    context=context,
                )
            )

        return results
