from core.planner.planning_context import PlanningContext
from core.planner.planning_pipeline import PlanningPipeline

from core.planner.stages.prompt_parser_stage import PromptParserStage
from core.planner.stages.intent_classifier_stage import IntentClassifierStage
from core.planner.stages.capability_planner_stage import CapabilityPlannerStage


pipeline = PlanningPipeline(

    [

        PromptParserStage(),

        IntentClassifierStage(),

        CapabilityPlannerStage(),

    ]

)

context = PlanningContext(

    prompt="""
    Build a modern AI SaaS with login,
    JWT authentication,
    dashboards,
    PostgreSQL,
    and AI assistants.
    """

)

pipeline.run(context)

print()

print(context.parsed)

print()

print(context.intent)

print()

print(context.capabilities)
