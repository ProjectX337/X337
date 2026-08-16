from core.intelligence.react_analyzer import (
    ReactAnalyzer,
)

from core.intelligence.application_snapshot import (
    ApplicationSnapshot,
)


def test_react_analyzer_detects_structure():

    snapshot = ApplicationSnapshot(
        project_name="demo",
        root_path="demo",
        files=[
            "src/pages/Home.tsx",
            "src/components/Button.tsx",
            "src/features/auth/pages/Login.tsx",
            "src/hooks/useAuth.ts",
        ],
    )


    result = ReactAnalyzer().analyze(
        snapshot
    )


    assert "Home" in result["pages"]

    assert "Button" in result["components"]

    assert "auth" in result["features"]

    assert "useAuth" in result["hooks"]
