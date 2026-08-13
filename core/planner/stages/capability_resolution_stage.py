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

    requires = set()

    provides = {
        "resolved_capabilities",
    }

    def __init__(self):
        self.resolver = CapabilityResolution()

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        hypotheses = [
            CapabilityHypothesis(
                name=name,
                confidence=0.5,
                source="capability_reasoner",
            )
            for name in context.capability_candidates
        ]

        if not hypotheses:
            hypotheses = context.capability_hypotheses

        context.resolved_capabilities = (
            self.resolver.resolve(
                hypotheses
            )
        )
