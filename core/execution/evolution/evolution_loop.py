from __future__ import annotations

from core.execution.evolution.evolution_engine import (
    EvolutionEngine,
)
from core.execution.coordinator import (
    ExecutionCoordinator,
)
from core.execution.signals.execution_signal import (
    ExecutionSignal,
)


class EvolutionLoop:
    """
    Closed-loop execution improvement cycle.

    Signal
       |
       v
    Evolution
       |
       v
    ChangePlan
       |
       v
    Execution
    """

    def __init__(
        self,
        evolution_engine: EvolutionEngine | None = None,
        coordinator: ExecutionCoordinator | None = None,
    ):

        self.evolution_engine = (
            evolution_engine
            or EvolutionEngine()
        )

        self.coordinator = coordinator


    def process(
        self,
        signal: ExecutionSignal,
        context=None,
    ):

        plan = self.evolution_engine.evolve(
            signal
        )

        if plan is None:
            return None

        if self.coordinator is None:
            return plan

        return self.coordinator.execute(
            plan,
            context=context,
        )
