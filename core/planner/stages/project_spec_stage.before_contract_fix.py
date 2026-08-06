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

            framework=(
                context.stack.frontend
                or context.stack.backend
                or context.stack.ai
                or context.stack.static_site
                or context.stack.scripting
                or context.stack.mobile
                or context.stack.desktop
                or ""
            ),

            path="",


            architecture=(
                context.stack.frontend
                or context.stack.backend
                or context.stack.ai
                or context.stack.static_site
                or context.stack.scripting
                or context.stack.mobile
                or context.stack.desktop
                or ""
            ),


            features=[
                feature.name
                for feature in context.feature_models
            ],


            description=context.parsed.description,


            language="",


            technologies=(
                context.technologies
                if context.technologies
                else None
            ),


            plan={},


            metadata={

                "capabilities": [
                    match.capability.name
                    for match in context.capabilities
                ],

                "task_graph": getattr(
                    context,
                    "task_graph",
                    None,
                ),

            },

        )
