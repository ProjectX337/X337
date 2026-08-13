from __future__ import annotations

from core.execution.intelligence.models import (
    ExecutionIntelligenceResult,
)


class ExecutionIntelligenceEngine:
    """
    Coordinates execution intelligence processing.

    Pipeline:

        ExecutionReport
              |
              v
        Memory Persistence
              |
              v
        Historical Analysis
              |
              v
        Evolution Signals
              |
              v
        Evolution Loop
    """

    def __init__(
        self,
        report_memory_sink,
        report_history_analyzer,
        report_evolution_bridge,
    ):
        self.report_memory_sink = report_memory_sink
        self.report_history_analyzer = report_history_analyzer
        self.report_evolution_bridge = report_evolution_bridge

    def process(
        self,
        report,
        context=None,
    ):
        self.report_memory_sink.store(
            report,
        )

        history = (
            self.report_memory_sink.memory.history()
        )

        analysis = self.report_history_analyzer.analyze(
            history,
        )

        signals = (
            self.report_evolution_bridge
            .feedback_processor
            .process(
                analysis
            )
        )

        evolution_results = (
            self.report_evolution_bridge.process(
                analysis,
                context=context,
            )
        )

        intelligence_result = ExecutionIntelligenceResult(
            analysis=analysis,
            evolution_plan=evolution_results,
            signals=signals,
            confidence=1.0,
        )

        report.feedback = intelligence_result.analysis
        report.evolution_plan = intelligence_result.evolution_plan

        return report
