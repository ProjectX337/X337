from pathlib import Path

from core.intelligence.application_scanner import (
    ApplicationScanner,
)


def test_application_scanner_reads_project(tmp_path):

    project = tmp_path / "demo"

    project.mkdir()

    (project / "package.json").write_text(
        "{}"
    )

    (project / "App.tsx").write_text(
        "export default App"
    )


    scanner = ApplicationScanner()

    snapshot = scanner.scan(
        str(project)
    )


    assert snapshot.project_name == "demo"

    assert (
        "package.json"
        in snapshot.files
    )

    assert (
        snapshot.language
        == "typescript"
    )

    assert (
        snapshot.framework
        == "javascript"
    )
