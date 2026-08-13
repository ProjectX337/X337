from core.capabilities.capability_registry import CapabilityRegistry
from core.graph.normalization.capability_normalizer import (
    CapabilityNormalizer,
)


def test_chat_capability_normalizes_to_ai():

    registry = CapabilityRegistry()

    capabilities = [
        registry.get("ai"),
        registry.get("chat"),
    ]

    normalized = CapabilityNormalizer().normalize(
        capabilities
    )

    slugs = {
        capability.slug
        for capability in normalized
    }

    assert "ai" in slugs
    assert "chat" not in slugs
