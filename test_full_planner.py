from core.planner.project_planner import ProjectPlanner

planner = ProjectPlanner()

spec = planner.plan(
    """
    Build a modern AI SaaS with:

    - AI assistants

    - PostgreSQL

    - Authentication

    - Dashboards

    - REST APIs
    """
)

print()

print("PROJECT SPEC")

print("=" * 50)

print()

print("Architecture")

print(spec.architecture)

print()

print("Technologies")

print(spec.technologies)

print()

print("Capabilities")

for capability in spec.capabilities:

    print(

        capability.capability.name,

        capability.score,

    )
