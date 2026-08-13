from core.intelligence.artifacts.capability_hypothesis import (
    CapabilityHypothesis,
)


def test_capability_hypothesis_contract():

    hypothesis = CapabilityHypothesis(
        name="adaptive tutoring",
        rationale=(
            "Students need personalized instruction"
        ),
        confidence=0.85,
    )

    assert (
        hypothesis.name
        == "adaptive tutoring"
    )

    assert (
        hypothesis.confidence
        == 0.85
    )

    assert (
        hypothesis.source
        == "product_intelligence"
    )
