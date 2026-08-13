from __future__ import annotations

from core.execution.signals.execution_signal import (
    ExecutionSignal,
)
from core.execution.evolution.signal_router import (
    SignalRouter,
)


class EvolutionEngine:
    """
    Converts execution signals into evolution plans.
    """

    def __init__(
        self,
        router: SignalRouter | None = None,
    ):

        self.router = (
            router
            or SignalRouter()
        )


    def evolve(
        self,
        signal: ExecutionSignal,
    ):

        return self.router.route(
            signal
        )
