from core.intelligence.models import ProductUnderstanding
from core.intelligence.reasoning.capability_reasoner import (
    CapabilityReasoner,
)


def test_capability_reasoner_generates_capabilities():

    understanding = ProductUnderstanding(
        domain="education",
        goals=[
            "Create an AI tutor application"
        ],
    )

    capabilities = (
        CapabilityReasoner()
        .reason(understanding)
    )

    assert (
        "adaptive tutoring"
        in capabilities
    )

    assert (
        "progress tracking"
        in capabilities
    )
