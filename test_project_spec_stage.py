from core.planner.models import (
    Intent,
    ParsedPrompt,
    TechnologyPlan,
)
from core.planner.planning_context import PlanningContext
from core.planner.stack_builder import ArchitectureStack
from core.planner.stages.project_spec_stage import ProjectSpecStage

context = PlanningContext(
    prompt="Build an AI SaaS"
)

context.parsed = ParsedPrompt(
    original=context.prompt
)

context.intent = Intent()

context.stack = ArchitectureStack()

context.technologies = TechnologyPlan()

ProjectSpecStage().run(context)

print(context.project_spec)
