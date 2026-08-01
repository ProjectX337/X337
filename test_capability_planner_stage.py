from core.planner.planning_context import PlanningContext
from core.planner.stages.prompt_parser_stage import PromptParserStage
from core.planner.stages.capability_planner_stage import CapabilityPlannerStage

context = PlanningContext(
    prompt="""
    Build a modern AI SaaS.

    User login.

    JWT authentication.

    AI assistant.

    Dashboard.
    """
)

PromptParserStage().run(context)

CapabilityPlannerStage().run(context)

print("Capability Matches:")

for match in context.capabilities:

    print()

    print(match.capability.name)

    print("score:", match.score)

    print("confidence:", match.confidence)

    print("technologies:", match.capability.technologies)
