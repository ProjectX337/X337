from __future__ import annotations


class ReportHistoryAnalyzer:
    """
    Analyzes historical execution memory.

    Converts execution history into
    reusable engineering intelligence.
    """

    def analyze(
        self,
        entries,
    ):

        total = len(entries)

        successes = [
            entry
            for entry in entries
            if entry.success
        ]

        failures = total - len(successes)

        return {
            "total_entries": total,
            "successful_entries": len(successes),
            "failed_entries": failures,
            "failure_rate": (
                failures / total
                if total
                else 0.0
            ),
        }
