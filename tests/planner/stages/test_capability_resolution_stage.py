from core.cognition.cognitive_state import CognitiveState

from core.intelligence.artifacts.capability_hypothesis import (
    CapabilityHypothesis,
)

from core.planner.stages.capability_resolution_stage import (
    CapabilityResolutionStage,
)


def test_capability_resolution_stage():

    state = CognitiveState(
        prompt="AI Tutor"
    )

    state.capability_hypotheses = [
        CapabilityHypothesis(
            name="adaptive tutoring",
            confidence=0.85,
        )
    ]

    CapabilityResolutionStage().run(
        state
    )

    assert (
        state.resolved_capabilities[0].name
        == "adaptive tutoring"
    )
