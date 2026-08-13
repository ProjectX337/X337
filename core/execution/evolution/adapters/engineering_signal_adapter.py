from __future__ import annotations

from core.execution.signals.execution_signal import (
    ExecutionSignal,
)

from core.graph.signals import (
    EngineeringSignal,
    SignalType,
)


class EngineeringSignalAdapter:
    """
    Converts legacy execution signals
    into canonical engineering signals.
    """

    def convert(
        self,
        signal,
    ) -> EngineeringSignal:

        if isinstance(
            signal,
            EngineeringSignal,
        ):
            return signal

        return EngineeringSignal(
            signal_type=self._map_type(
                signal.signal_type
            ),
            target_node=signal.action,
            metadata={
                "reason": signal.message,
                "severity": signal.severity,
            },
        )


    def _map_type(
        self,
        signal_type: str,
    ) -> SignalType:

        if signal_type == "unstable_capability":
            return SignalType.MODIFY_COMPONENT

        if signal_type == "run_tests":
            return SignalType.RUN_TESTS

        return SignalType.MODIFY_COMPONENT
