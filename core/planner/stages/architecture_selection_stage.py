from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.planner.architecture_selector import ArchitectureSelector
from core.planner.stages.base_stage import PlanningStage


class ArchitectureSelectionStage(PlanningStage):
    """
    Selects architecture candidates from canonical
    ArchitectureRequirements.

    Contract:

        architecture_requirements
            ↓
        architecture_candidates
    """

    requires = {
        "architecture_requirements",
    }

    provides = {
        "architecture_candidates",
    }

    def __init__(self) -> None:
        self.selector = ArchitectureSelector()

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        if context.architecture_requirements is None:
            raise RuntimeError(
                "ArchitectureSelectionStage requires "
                "architecture_requirements."
            )

        context.architecture_candidates = self.selector.select(
            context.architecture_requirements
        )
