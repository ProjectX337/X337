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

            prompt=context.prompt,

            parsed=context.parsed,

            intent=context.intent,

            architecture=context.stack,

            capabilities=context.capabilities,

            feature_models=context.feature_models,

            technologies=context.technologies,

            name=context.parsed.project_name,

            framework=(
                context.technologies.frontend
                if context.technologies
                else ""
            ),

            path="",

            language="",

            plan={},

            metadata={},

            ui_spec=context.ui_spec,
            task_graph=context.task_graph,

        )
