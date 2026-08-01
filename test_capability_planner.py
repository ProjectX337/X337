from core.planner.prompt_parser import PromptParser
from core.planner.capability_planner import CapabilityPlanner

parser = PromptParser()
planner = CapabilityPlanner()

parsed = parser.parse(
    """
    Build an AI SaaS.

    Authentication.

    Login.

    JWT.

    AI assistant.

    Authentication.

    Dashboard.
    """
)

matches = planner.plan(parsed)

for match in matches:

    print()

    print(match.capability.name)

    print("score:", match.score)

    print("confidence:", match.confidence)

    print("technologies:", match.capability.technologies)
