from __future__ import annotations

from core.execution.runtime.execution_runtime import (
    ExecutionRuntime,
)

from core.execution.coordinator import (
    ExecutionCoordinator,
)

from core.execution.bootstrap.default_capabilities import (
    create_default_router,
)

from core.execution.evolution.evolution_loop import (
    EvolutionLoop,
)

from core.execution.evolution.evolution_engine import (
    EvolutionEngine,
)

from core.execution.learning.feedback_processor import (
    FeedbackProcessor,
)

from core.execution.memory.execution_memory import (
    ExecutionMemory,
)

from core.execution.events.event_bus import (
    ExecutionEventBus,
)

from core.execution.observability.execution_metrics import (
    ExecutionMetrics,
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

from core.execution.report.report_analyzer import (
    ExecutionReportAnalyzer,
)

from core.execution.report.report_feedback import (
    ReportFeedbackProcessor,
)

from core.execution.report.report_evolution_bridge import (
    ReportEvolutionBridge,
)


def create_execution_runtime():

    router = create_default_router()

    coordinator = ExecutionCoordinator(
        router=router,
    )

    evolution_engine = EvolutionEngine()

    evolution_loop = EvolutionLoop(
        evolution_engine=evolution_engine,
        coordinator=coordinator,
    )

    memory = ExecutionMemory()

    feedback_processor = FeedbackProcessor(
        memory=memory,
    )

    event_bus = ExecutionEventBus()

    metrics = ExecutionMetrics()

    lifecycle = RuntimeLifecycle(
        event_bus=event_bus,
        metrics=metrics,
        feedback_processor=feedback_processor,
    )

    report_collector = ExecutionReportCollector()

    report_enricher = ExecutionReportEnricher()

    report_memory_sink = ReportMemorySink(
        memory=memory,
    )

    report_analyzer = ExecutionReportAnalyzer()

    report_feedback_processor = ReportFeedbackProcessor()

    report_evolution_bridge = ReportEvolutionBridge(
        feedback_processor=report_feedback_processor,
        evolution_loop=evolution_loop,
    )

    return ExecutionRuntime(
        coordinator=coordinator,
        evolution_loop=evolution_loop,
        feedback_processor=feedback_processor,
        lifecycle=lifecycle,
        report_collector=report_collector,
        report_enricher=report_enricher,
        report_memory_sink=report_memory_sink,
        report_analyzer=report_analyzer,
        report_feedback_processor=report_feedback_processor,
        report_evolution_bridge=report_evolution_bridge,
    )
