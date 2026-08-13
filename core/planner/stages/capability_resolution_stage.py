from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.intelligence.artifacts.capability_hypothesis import CapabilityHypothesis
from core.intelligence.resolution.capability_resolution import (
    CapabilityResolution,
)

from core.planner.stages.base_stage import PlanningStage


class CapabilityResolutionStage(PlanningStage):
    """
    Converts intelligence capability hypotheses into
    resolved implementation capabilities.
    """

    requires = {
        "capability_hypotheses",
    }

    provides = {
        "resolved_capabilities",
    }

    def __init__(self):
        self.resolver = CapabilityResolution()

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        hypotheses = context.capability_hypotheses

        if not hypotheses:
            hypotheses = [
                CapabilityHypothesis(
                    name=name,
                    confidence=0.5,
                    source="compatibility",
                )
                for name in context.capability_candidates
            ]

        context.resolved_capabilities = (
            self.resolver.resolve(
                hypotheses
            )
        )
