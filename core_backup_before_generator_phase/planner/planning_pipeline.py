from __future__ import annotations

from typing import Iterable

from core.planner.planning_context import PlanningContext
from core.planner.stages.base_stage import PlanningStage


class PlanningPipeline:
    """
    Executes planning stages in order.

    Validates stage dependencies before execution.
    """

    def __init__(
        self,
        stages: Iterable[PlanningStage],
    ):

        self.stages = list(stages)

    # ---------------------------------------------------------

    def _validate_stage(
        self,
        stage: PlanningStage,
        context: PlanningContext,
    ) -> None:

        for field in stage.requires:

            if getattr(context, field) is None:

                raise RuntimeError(

                    f"{stage.__class__.__name__} "

                    f"requires context.{field}"

                )

    # ---------------------------------------------------------

    def run(
        self,
        context: PlanningContext,
    ) -> PlanningContext:

        for stage in self.stages:

            self._validate_stage(
                stage,
                context,
            )

            stage.run(
                context,
            )

        return context
