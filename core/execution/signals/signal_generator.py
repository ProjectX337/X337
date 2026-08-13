from __future__ import annotations

from core.execution.signals.execution_signal import (
    ExecutionSignal,
)


class ExecutionSignalGenerator:
    """
    Converts execution memory patterns into
    architectural improvement signals.
    """

    def generate(
        self,
        memory,
        action: str,
    ) -> ExecutionSignal | None:

        rate = memory.success_rate(
            action
        )

        if rate < 0.5:

            return ExecutionSignal(
                signal_type="unstable_capability",
                action=action,
                target="runtime",
                severity=1.0 - rate,
                message=(
                    f"{action} has low success rate"
                ),
            )

        return None
