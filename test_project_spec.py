from core.spec.project_spec import ProjectSpec
from core.planner.models import (
    ParsedPrompt,
    Intent,
    TechnologyPlan,
)
from core.planner.stack_builder import ArchitectureStack

spec = ProjectSpec(
    prompt="Build an AI SaaS",
    parsed=ParsedPrompt(
        original="Build an AI SaaS"
    ),
    intent=Intent(),
    architecture=ArchitectureStack(),
    technologies=TechnologyPlan(),
)

print(spec)
