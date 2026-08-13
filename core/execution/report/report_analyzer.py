from __future__ import annotations


class ExecutionReportAnalyzer:
    """
    Analyzes execution reports to extract
    reusable execution intelligence.
    """

    def analyze(
        self,
        reports,
    ):

        total = len(reports)

        successes = [
            report
            for report in reports
            if report.result is not None
        ]

        return {
            "total_reports": total,
            "successful_reports": len(successes),
            "success_rate": (
                len(successes) / total
                if total
                else 0.0
            ),
        }
