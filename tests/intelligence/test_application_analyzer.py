from core.intelligence.application_snapshot import (
    ApplicationSnapshot,
)

from core.intelligence.application_analyzer import (
    ApplicationAnalyzer,
)


def test_application_analyzer_creates_report():

    snapshot = ApplicationSnapshot(
        project_name="demo",
        root_path="/tmp/demo",
        framework="javascript",
        language="typescript",
        files=[
            "App.tsx",
            "package.json",
        ],
        components=[
            "App",
        ],
        pages=[
            "Home",
        ],
    )

    analyzer = ApplicationAnalyzer()

    report = analyzer.analyze(
        snapshot
    )

    assert report.project_name == "demo"

    assert report.file_count == 2

    assert report.component_count == 1

    assert report.page_count == 1

    assert report.score > 0
