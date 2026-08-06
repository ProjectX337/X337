from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.planner.stages.base_stage import PlanningStage
from core.spec.project_spec import ProjectSpec


class ProjectSpecStage(PlanningStage):
    """
    Builds the final ProjectSpec from the CognitiveState.
    """

    requires = {
        "parsed",
        "intent",
        "stack",
        "technologies",
        "feature_models",
    }

    provides = {
        "project_spec",
    }

    # ---------------------------------------------------------

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.project_spec = ProjectSpec(

            name=context.parsed.project_name,

            framework="",

            path="",

            architecture=context.stack,

            features=[
                feature.name
                for feature in context.feature_models
            ],

            description=context.parsed.description,

            plan={},

            metadata={
                "capabilities": [
                    match.capability.name
                    for match in context.capabilities
                ],
                "technologies": context.technologies,
                "ui_spec": context.ui_spec,
                "task_graph": context.task_graph,
            },

        ),

            path="",

            language="",

            plan={},

            metadata={},

            ui_spec=context.ui_spec,
            task_graph=context.task_graph,

        )
