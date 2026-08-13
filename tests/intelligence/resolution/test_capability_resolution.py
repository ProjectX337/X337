from core.intelligence.artifacts.capability_hypothesis import (
    CapabilityHypothesis,
)

from core.intelligence.resolution.capability_resolution import (
    CapabilityResolution,
)


def test_capability_resolution_converts_hypothesis():

    hypothesis = CapabilityHypothesis(
        name="adaptive tutoring",
        confidence=0.85,
    )

    result = (
        CapabilityResolution()
        .resolve(
            [hypothesis]
        )
    )

    assert (
        result[0].name
        == "adaptive tutoring"
    )

    assert (
        "progress tracking"
        in result[0].features
    )
