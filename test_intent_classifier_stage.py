from core.planner.planning_context import PlanningContext
from core.planner.stages.prompt_parser_stage import PromptParserStage
from core.planner.stages.intent_classifier_stage import IntentClassifierStage

context = PlanningContext(
    prompt="Build a modern AI SaaS with authentication, PostgreSQL, dashboards and REST APIs."
)

PromptParserStage().run(context)

IntentClassifierStage().run(context)

print(context.intent)
