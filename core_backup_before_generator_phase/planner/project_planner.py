from __future__ import annotations

from core.planner.planning_context import PlanningContext
from core.planner.planning_pipeline import PlanningPipeline

from core.planner.stages.prompt_parser_stage import PromptParserStage
from core.planner.stages.intent_classifier_stage import IntentClassifierStage
from core.planner.stages.capability_planner_stage import CapabilityPlannerStage
from core.planner.stages.feature_stage import FeatureStage
from core.planner.stages.architecture_selection_stage import (
    ArchitectureSelectionStage,
)
from core.planner.stages.stack_builder_stage import (
    StackBuilderStage,
)
from core.planner.stages.technology_resolver_stage import (
    TechnologyResolverStage,
)
from core.planner.stages.project_spec_stage import (
    ProjectSpecStage,
)

from core.planner.stages.ui_spec_stage import (
    UISpecStage,
)


class ProjectPlanner:
    """
    Public API for the planning engine.
    """

    def __init__(self):

        self.pipeline = PlanningPipeline(

            [

                PromptParserStage(),

                IntentClassifierStage(),

                CapabilityPlannerStage(),

            FeatureStage(),

                ArchitectureSelectionStage(),

                StackBuilderStage(),

                TechnologyResolverStage(),

                UISpecStage(),
                ProjectSpecStage(),

            ]

        )

    # ---------------------------------------------------------

    def create_context(
        self,
        prompt: str,
    ) -> PlanningContext:

        return PlanningContext(
            prompt=prompt,
        )

    # ---------------------------------------------------------

    def plan_context(
        self,
        prompt: str,
    ) -> PlanningContext:

        context = self.create_context(
            prompt,
        )

        return self.pipeline.run(
            context,
        )

    # ---------------------------------------------------------

    def plan(
        self,
        prompt: str,
    ):

        context = self.plan_context(
            prompt,
        )

        if context.project_spec is None:

            raise RuntimeError(
                "ProjectSpec was not produced."
            )

        return context.project_spec
