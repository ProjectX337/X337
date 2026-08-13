from core.cognition.cognitive_state import (
    CognitiveState,
)

from core.intelligence.artifacts.capability_hypothesis import (
    CapabilityHypothesis,
)


def test_cognitive_state_supports_capability_hypotheses():

    state = CognitiveState(
        prompt="AI Tutor"
    )

    state.capability_hypotheses = [
        CapabilityHypothesis(
            name="adaptive tutoring",
            confidence=0.85,
        )
    ]

    assert (
        state.capability_hypotheses[0].name
        == "adaptive tutoring"
    )
