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

        resolved: dict[str, ResolvedCapability] = {}
        visited: set[str] = set()

        def expand(
            name: str,
            confidence: float,
            source: str,
        ) -> None:

            if name in visited:
                return

            visited.add(name)

            capability = self.registry.get(name)

            if capability is None:
                resolved[name] = ResolvedCapability(
                    name=name,
                    capability=None,
                    features=self.mappings.get(
                        name,
                        [],
                    ),
                    confidence=confidence,
                    source=source,
                )

                return

            resolved[name] = ResolvedCapability(
                name=name,
                capability=capability,
                features=self.mappings.get(
                    name,
                    [],
                ),
                confidence=confidence,
                source=source,
            )

            for dependency in capability.depends_on:
                expand(
                    dependency,
                    confidence,
                    "dependency_resolution",
                )

            for implication in capability.implies:
                expand(
                    implication,
                    confidence,
                    "implication_resolution",
                )

        for hypothesis in hypotheses:
            expand(
                hypothesis.name,
                hypothesis.confidence,
                hypothesis.source,
            )

        return list(
            resolved.values()
        )
