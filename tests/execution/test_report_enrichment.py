from core.execution.report.execution_report import (
    ExecutionReport,
)

from core.execution.report.report_enricher import (
    ExecutionReportEnricher,
)


def test_report_enrichment():

    report = ExecutionReport(
        execution_id="exec-1",
        plan="plan",
    )

    enricher = ExecutionReportEnricher()

    result = enricher.enrich(
        report,
        feedback="feedback",
        signals=["signal"],
        evolution_plan="change",
        events=["event"],
    )

    assert result.feedback == "feedback"
    assert result.signals == ["signal"]
    assert result.evolution_plan == "change"
    assert result.events == ["event"]
