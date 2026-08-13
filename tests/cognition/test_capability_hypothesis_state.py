from dataclasses import fields

from core.cognition.cognitive_state import (
    CognitiveState,
)


def test_cognitive_state_has_capability_hypothesis_contract():

    names = {
        field.name
        for field in fields(
            CognitiveState
        )
    }

    assert (
        "capability_hypotheses"
        in names
    )
