from __future__ import annotations

from uuid import uuid4

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

from core.execution.report.report_collector import (
    ExecutionReportCollector,
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
        report_collector: ExecutionReportCollector,
    ):

        self.coordinator = coordinator
        self.evolution_loop = evolution_loop
        self.feedback_processor = feedback_processor
        self.lifecycle = lifecycle
        self.report_collector = report_collector


    def execute(
        self,
        plan,
        context=None,
    ):

        execution_id = str(uuid4())

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

        return self.report_collector.collect(
            execution_id=execution_id,
            plan=plan,
            result=result,
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
