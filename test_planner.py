from core.planner.planner import Planner

planner = Planner()

result = planner.plan(
    "Build a modern AI SaaS with authentication, PostgreSQL, dashboards and an AI assistant."
)

print("Architecture:")
print(result.architecture)

print()

print("Framework:")
print(result.framework)

print()

print("Technology Plan:")
print(result.technologies)
