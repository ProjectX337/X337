from core.planner.planning_context import PlanningContext
from core.planner.stages.prompt_parser_stage import PromptParserStage

context = PlanningContext(
    prompt="Build a modern AI SaaS with authentication."
)

stage = PromptParserStage()

stage.run(context)

print(context.parsed)
