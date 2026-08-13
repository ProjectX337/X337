from __future__ import annotations

from core.execution.coordinator import (
    ExecutionCoordinator,
)

from core.execution.evolution.evolution_loop import (
    EvolutionLoop,
)

from core.execution.learning.feedback_processor import (
    FeedbackProcessor,
)

from core.execution.lifecycle.runtime_lifecycle import (
    RuntimeLifecycle,
)


class ExecutionRuntime:
    """
    Unified execution intelligence runtime.

    Owns:
        execution
        feedback
        learning
        evolution
    """

    def __init__(
        self,
        coordinator: ExecutionCoordinator,
        evolution_loop: EvolutionLoop,
        feedback_processor: FeedbackProcessor,
        lifecycle: RuntimeLifecycle,
    ):

        self.coordinator = coordinator
        self.evolution_loop = evolution_loop
        self.feedback_processor = feedback_processor
        self.lifecycle = lifecycle


    def execute(
        self,
        plan,
        context=None,
    ):

        self.lifecycle.before(
            plan
        )

        result = self.coordinator.execute(
            plan,
            context=context,
        )

        self.lifecycle.after(
            result,
            plan,
        )

        return result


    def learn(
        self,
        feedback,
    ):

        return self.feedback_processor.process(
            feedback
        )


    def evolve(
        self,
        signal,
        context=None,
    ):

        return self.evolution_loop.process(
            signal,
            context=context,
        )
