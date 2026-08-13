from core.execution.bootstrap.runtime_factory import (
    create_execution_runtime,
)

from core.graph.signals import SignalType


def test_historical_reports_trigger_evolution_signal():

    runtime = create_execution_runtime()

    runtime.report_memory_sink.memory.remember(
        type(
            "Entry",
            (),
            {
                "action": "component",
                "target": "A",
                "success": False,
            },
        )()
    )

    analysis = (
        runtime.report_history_analyzer.analyze(
            runtime.report_memory_sink.memory.history()
        )
    )

    results = (
        runtime.report_evolution_bridge.process(
            analysis
        )
    )

    assert len(results) == 1