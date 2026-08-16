from core.intelligence.application_understanding import (
    ApplicationUnderstanding,
)

from core.intelligence.application_snapshot import (
    ApplicationSnapshot,
)


def test_application_understanding():

    snapshot = ApplicationSnapshot(
        project_name="demo",
        root_path="demo",
        framework="javascript",
        language="typescript",
        files=[
            "src/pages/Home.tsx",
        ],
    )


    result = ApplicationUnderstanding().understand(
        snapshot
    )


    assert result["project"] == "demo"

    assert result["react"]["pages"] == [
        "Home"
    ]
