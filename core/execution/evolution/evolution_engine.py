from __future__ import annotations

from core.execution.signals.execution_signal import (
    ExecutionSignal,
)

from core.execution.evolution.signal_router import (
    SignalRouter,
)

from core.execution.evolution.adapters.engineering_signal_adapter import (
    EngineeringSignalAdapter,
)

from core.graph.signals import (
    EngineeringSignal,
)


class EvolutionEngine:
    """
    Converts execution intelligence into
    canonical engineering evolution plans.
    """

    def __init__(
        self,
        router: SignalRouter | None = None,
    ):

        self.router = (
            router
            or SignalRouter()
        )

        self.adapter = (
            EngineeringSignalAdapter()
        )


    def evolve(
        self,
        signal,
    ):

        if isinstance(
            signal,
            ExecutionSignal,
        ):
            signal = self.adapter.convert(
                signal
            )

        return self.router.route(
            signal
        )
