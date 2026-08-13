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

from core.execution.report.report_enricher import (
    ExecutionReportEnricher,
)

from core.execution.report.report_memory_sink import (
    ReportMemorySink,
)

from core.execution.report.report_feedback import (
    ReportFeedbackProcessor,
)

from core.execution.report.report_analyzer import (
    ExecutionReportAnalyzer,
)

from core.execution.report.report_enricher import (
    ExecutionReportEnricher,
)


class ExecutionRuntime:
    """
    Unified execution intelligence runtime.

    Owns:
        execution
        reporting
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
        report_enricher: ExecutionReportEnricher,
        report_memory_sink: ReportMemorySink,
        report_analyzer: ExecutionReportAnalyzer,
        report_feedback_processor,
    ):

        self.coordinator = coordinator
        self.evolution_loop = evolution_loop
        self.feedback_processor = feedback_processor
        self.lifecycle = lifecycle
        self.report_collector = report_collector
        self.report_enricher = report_enricher
        self.report_memory_sink = report_memory_sink
        self.report_feedback_processor = report_feedback_processor
        self.report_analyzer = report_analyzer


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

        report = self.report_collector.collect(
            execution_id=execution_id,
            plan=plan,
            result=result,
        )

        return self.report_enricher.enrich(
            report,
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
