from __future__ import annotations

from core.graph.change_plan import (
    ChangePlan,
    ChangeRequest,
)

from core.graph.change import (
    ChangeType,
)

from core.graph.signals import (
    EngineeringSignal,
    SignalType,
)

from core.execution.signals.execution_signal import (
    ExecutionSignal,
)

from core.execution.evolution.adapters.engineering_signal_adapter import (
    EngineeringSignalAdapter,
)



class SignalRouter:
    """
    Converts engineering signals into evolution plans.
    """

    def route(
        self,
        signal,
    ) -> ChangePlan | None:

        if isinstance(
            signal,
            ExecutionSignal,
        ):
            signal = EngineeringSignalAdapter().convert(
                signal
            )

        if signal.signal_type in (
            SignalType.MODIFY_COMPONENT,
            SignalType.RUN_TESTS,
        ):

            return ChangePlan(
                change=ChangeRequest(
                    target_node=signal.target_node,
                    change_type=ChangeType.MODIFY,
                )
            )

        return None
