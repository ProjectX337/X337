from core.capabilities.capability_registry import (
    CapabilityRegistry,
)

from core.graph.normalization.capability_normalizer import (
    CapabilityNormalizer,
)


def test_capability_alias_preserves_dependencies():

    registry = CapabilityRegistry()

    capabilities = [
        registry.get("chat"),
        registry.get("ai"),
        registry.get("authentication"),
    ]

    normalized = (
        CapabilityNormalizer()
        .normalize(
            capabilities
        )
    )


    ai = next(
        c for c in normalized
        if c.slug == "ai"
    )


    assert (
        "authentication"
        in ai.depends_on
    )
