from core.planner.planning_context import PlanningContext

from core.planner.stages.prompt_parser_stage import PromptParserStage
from core.planner.stages.intent_classifier_stage import IntentClassifierStage
from core.planner.stages.capability_planner_stage import CapabilityPlannerStage
from core.planner.stages.architecture_selection_stage import (
    ArchitectureSelectionStage,
)
from core.planner.stages.stack_builder_stage import (
    StackBuilderStage,
)
from core.planner.stages.technology_resolver_stage import (
    TechnologyResolverStage,
)

context = PlanningContext(
    prompt="""
    Build a modern AI SaaS with authentication,
    PostgreSQL,
    dashboards,
    and AI assistants.
    """
)

PromptParserStage().run(context)
IntentClassifierStage().run(context)
CapabilityPlannerStage().run(context)
ArchitectureSelectionStage().run(context)
StackBuilderStage().run(context)
TechnologyResolverStage().run(context)

print()

print(context.technologies)
