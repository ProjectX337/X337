from core.cognition.cognitive_state import (
    CognitiveState,
)

from core.graph.evolution.models import (
    EvolutionPlan,
)


def test_cognitive_state_supports_evolution_plan():

    state = CognitiveState(
        prompt="Add MFA authentication"
    )

    state.evolution_plan = EvolutionPlan(
        actions=[
            "add MFA component"
        ]
    )

    assert (
        state.evolution_plan.actions[0]
        == "add MFA component"
    )
