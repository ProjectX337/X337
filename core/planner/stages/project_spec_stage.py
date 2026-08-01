from __future__ import annotations

from core.planner.planning_context import PlanningContext
from core.planner.stages.base_stage import PlanningStage
from core.spec.project_spec import ProjectSpec


class ProjectSpecStage(PlanningStage):
    """
    Builds the final ProjectSpec from the PlanningContext.
    """

    requires = {
        "parsed",
        "intent",
        "stack",
        "technologies",
    }

    provides = {
        "project_spec",
    }

    # ---------------------------------------------------------

    def run(
        self,
        context: PlanningContext,
    ) -> None:

        context.project_spec = ProjectSpec(

            prompt=context.prompt,

            parsed=context.parsed,

            intent=context.intent,

            architecture=context.stack,

            capabilities=context.capabilities,

            technologies=context.technologies,

        ui_spec=context.ui_spec,

        )
