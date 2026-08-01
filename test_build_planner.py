from core.build.build_planner import BuildPlanner
from core.planner.project_planner import ProjectPlanner

planner = ProjectPlanner()

spec = planner.plan(
    """
    Build a modern AI SaaS with
    authentication,
    PostgreSQL,
    dashboards,
    and AI assistants.
    """
)

plan = BuildPlanner().build(spec)

print()

print("BUILD PLAN")

print("=" * 60)

for step in plan.ordered_steps():

    print(f"Step: {step.name}")

    print(f"Generator : {step.generator}")

    print(f"Directory : {step.output_directory}")

    print(f"Priority  : {step.priority}")

    print(f"Depends On: {step.depends_on}")

    print(f"Optional  : {step.optional}")

    print()
