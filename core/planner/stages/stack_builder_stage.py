from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.planner.stages.base_stage import PlanningStage
from core.planner.stack_builder import StackBuilder


class StackBuilderStage(PlanningStage):
    """
    Builds the final architecture stack from ranked
    architecture candidates and canonical requirements.
    """

    requires = {
        "architecture_requirements",
        "architecture_candidates",
    }

    provides = {
        "stack",
    }

    def __init__(self) -> None:
        self.builder = StackBuilder()

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        if context.architecture_requirements is None:
            raise RuntimeError(
                "StackBuilderStage requires "
                "architecture_requirements."
            )

        context.stack = self.builder.build(
            context.architecture_candidates,
            context.architecture_requirements,
        )
