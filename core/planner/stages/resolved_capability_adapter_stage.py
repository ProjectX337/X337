from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.capabilities.capability_registry import CapabilityRegistry
from core.planner.capability_match import CapabilityMatch
from core.planner.stages.base_stage import PlanningStage


class ResolvedCapabilityAdapterStage(PlanningStage):
    """
    Converts intelligence-layer ResolvedCapability artifacts
    into planner CapabilityMatch objects.
    """

    requires = {
        "resolved_capabilities",
    }

    provides = {
        "capabilities",
    }

    def __init__(self) -> None:
        self.registry = CapabilityRegistry()

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.capabilities = []

        context.capability_models = []

        for resolved in context.resolved_capabilities:

            capability = self.registry.get(
                resolved.name
            )

            if capability is None:
                continue

            match = CapabilityMatch(
                capability=capability,
                score=int(
                    resolved.confidence * 5
                ),
                confidence=resolved.confidence,
            )

            context.capabilities.append(match)

            context.capability_models.append(
                capability
            )
