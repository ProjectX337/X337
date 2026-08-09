from __future__ import annotations

from core.planner.stages.base_stage import PlanningStage
from core.planner.context import CognitiveState
from core.spec.project_spec import ProjectSpec


class ProjectSpecStage(PlanningStage):

    name = "project_spec"

    requires = {
        "parsed",
        "intent",
        "capabilities",
        "feature_models",
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

            framework="",

            path="",

            architecture=context.stack
            if hasattr(context, "stack")
            else "",

            features=[
                feature.name
                for feature in context.feature_models
            ],

            description=context.parsed.description,

            language="",

            plan={},

            metadata={

                "capabilities": [
                    match.capability.name
                    for match in context.capabilities
                ],

                "technologies": getattr(
                    context,
                    "technologies",
                    [],
                ),

                "ui_spec": getattr(
                    context,
                    "ui_spec",
                    None,
                ),

                "task_graph": getattr(
                    context,
                    "task_graph",
                    None,
                ),

            },

        )
