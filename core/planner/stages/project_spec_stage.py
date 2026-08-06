from __future__ import annotations

from core.planner.stages.base_stage import PlanningStage
from core.cognition.cognitive_state import CognitiveState
from core.spec.project_spec import ProjectSpec


class ProjectSpecStage(PlanningStage):

    name = "project_spec"

    requires = {
        "parsed",
        "intent",
        "capabilities",
        "feature_models",
        "technologies",
    }

    provides = {
        "project_spec",
    }


    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.project_spec = ProjectSpec(

            name=context.parsed.project_name,

            parsed=context.parsed,

            intent=context.intent,

            architecture=getattr(
            context,
            "architecture",
            context.stack,
        ),

            capabilities=context.capabilities,

            technologies=context.technologies,

            feature_models=context.feature_models,

            ui_spec=context.ui_spec,

            design_spec=context.design_spec,

    

            framework=(
                context.stack.frontend
                or context.stack.backend
                or context.stack.ai
                or ""
            ),

            metadata={
                "task_graph": getattr(
                    context,
                    "task_graph",
                    None,
                ),
            },

        )
