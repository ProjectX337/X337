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
    ):

        self.coordinator = coordinator
        self.evolution_loop = evolution_loop
        self.feedback_processor = feedback_processor


    def execute(
        self,
        plan,
        context=None,
    ):

        return self.coordinator.execute(
            plan,
            context=context,
        )


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
