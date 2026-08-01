from core.planner.project_planner import ProjectPlanner

planner = ProjectPlanner()

context = planner.plan(
    """
    Build a modern AI SaaS with authentication,
    PostgreSQL,
    dashboards,
    and AI assistants.
    """
)

print()

print("Parsed:")
print(context.parsed)

print()

print("Intent:")
print(context.intent)

print()

print("Capabilities:")
for match in context.capabilities:

    print(
        f"- {match.capability.name} "
        f"(score={match.score}, confidence={match.confidence:.2f})"
    )
