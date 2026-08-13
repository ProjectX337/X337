from __future__ import annotations

from core.graph.change_plan import (
    ChangePlan,
    ChangeRequest,
)

from core.graph.change import (
    ChangeType,
)

from core.execution.signals.execution_signal import (
    ExecutionSignal,
)


class SignalRouter:
    """
    Converts runtime signals into evolution plans.

    Runtime:

        Signal
          |
          v
        ChangeRequest
          |
          v
        ChangePlan
    """

    def route(
        self,
        signal: ExecutionSignal,
    ) -> ChangePlan | None:

        if signal.signal_type == (
            "unstable_capability"
        ):

            return ChangePlan(
                change=ChangeRequest(
                    target_node=signal.action,
                    change_type=ChangeType.MODIFY,
                )
            )

        return None
