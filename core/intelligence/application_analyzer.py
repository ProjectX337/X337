from core.intelligence.application_snapshot import (
    ApplicationSnapshot,
)

from core.intelligence.application_report import (
    ApplicationReport,
)


class ApplicationAnalyzer:
    """
    Converts application observations
    into engineering intelligence.
    """

    def analyze(
        self,
        snapshot: ApplicationSnapshot,
    ) -> ApplicationReport:

        report = ApplicationReport(
            project_name=snapshot.project_name,
            framework=snapshot.framework,
            language=snapshot.language,
            file_count=len(snapshot.files),
            component_count=len(snapshot.components),
            page_count=len(snapshot.pages),
            dependency_count=len(
                snapshot.dependencies
            ),
        )

        self._analyze_structure(
            snapshot,
            report,
        )

        self._calculate_score(
            report
        )

        return report


    def _analyze_structure(
        self,
        snapshot,
        report,
    ):

        if not snapshot.files:
            report.findings.append(
                "Application contains no files"
            )

        if not snapshot.components:
            report.findings.append(
                "No components detected"
            )

        if snapshot.framework == "javascript":
            report.recommendations.append(
                "Detect frontend framework details"
            )


    def _calculate_score(
        self,
        report,
    ):

        score = 50

        if report.file_count:
            score += 10

        if report.page_count:
            score += 15

        if report.component_count:
            score += 15

        report.score = min(
            score,
            100,
        )
