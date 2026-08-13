from __future__ import annotations

from core.execution.signals.execution_signal import (
    ExecutionSignal,
)


class EngineeringSignalAdapter:
    """
    Converts canonical graph EngineeringSignals
    into legacy execution signals consumed by
    the evolution runtime.
    """

    def convert(
        self,
        signal,
    ) -> ExecutionSignal:

        return ExecutionSignal(
            signal_type=signal.signal_type.value,
            action=signal.target_node,
            target=signal.target_node,
            severity=1.0,
            message=(
                signal.metadata.get(
                    "reason",
                    "",
                )
            ),
        )
