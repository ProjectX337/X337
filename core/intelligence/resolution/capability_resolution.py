from dataclasses import dataclass, field

from core.capabilities.capability import Capability
from core.capabilities.capability_registry import CapabilityRegistry
from core.intelligence.artifacts.capability_hypothesis import (
    CapabilityHypothesis,
)


@dataclass
class ResolvedCapability:
    name: str

    capability: Capability | None = None

    features: list[str] = field(
        default_factory=list
    )

    confidence: float = 0.0

    source: str = "capability_resolution"


class CapabilityResolution:
    """
    Converts capability hypotheses into
    implementation-ready capabilities.
    """

    mappings = {
        "adaptive tutoring": [
            "progress tracking",
            "personalized recommendations",
            "lesson adaptation",
        ],
    }

    def __init__(self):
        self.registry = CapabilityRegistry()

    def resolve(
        self,
        hypotheses: list[CapabilityHypothesis],
    ) -> list[ResolvedCapability]:

        resolved = []

        for hypothesis in hypotheses:

            features = self.mappings.get(
                hypothesis.name,
                [],
            )

            capability = self.registry.get(
                hypothesis.name
            )

            resolved.append(
                ResolvedCapability(
                    name=hypothesis.name,
                    capability=capability,
                    features=features,
                    confidence=hypothesis.confidence,
                )
            )

        return resolved
