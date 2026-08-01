from core.planner.planning_context import PlanningContext

from core.planner.stages.prompt_parser_stage import PromptParserStage
from core.planner.stages.intent_classifier_stage import IntentClassifierStage
from core.planner.stages.architecture_selection_stage import (
    ArchitectureSelectionStage,
)
from core.planner.stages.stack_builder_stage import (
    StackBuilderStage,
)

context = PlanningContext(
    prompt="""
    Build a modern AI SaaS with
    authentication,
    PostgreSQL,
    dashboards,
    and AI assistants.
    """
)

PromptParserStage().run(context)

IntentClassifierStage().run(context)

ArchitectureSelectionStage().run(context)

StackBuilderStage().run(context)

print()

print(context.stack)
