from core.cognition.cognitive_state import (
    CognitiveState,
)

from core.planner.stages.product_intelligence_stage import (
    ProductIntelligenceStage,
)


def test_product_intelligence_stage():

    state = CognitiveState(
        prompt="AI Tutor"
    )

    ProductIntelligenceStage().execute(
        state
    )

    assert (
        state.product_understanding
        is not None
    )

    assert (
        state.product_spec
        is not None
    )

    assert (
        len(state.application_graph.nodes)
        > 0
    )
