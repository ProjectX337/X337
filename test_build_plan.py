from core.build.build_plan import BuildPlan

plan = BuildPlan()

plan.add(
    "Frontend",
    "react",
    "Generate the React application",
)

plan.add(
    "Backend",
    "fastapi",
    "Generate the FastAPI backend",
)

print(plan)
