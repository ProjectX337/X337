from core.planner.project_planner import ProjectPlanner
from core.execution.execution_planner import ExecutionPlanner


def test_execution_tasks_generated_from_change_plan():

    planner = ProjectPlanner()

    state = planner.plan_with_state(
        "Create an authentication dashboard application"
    )

    plan = state.change_plans[0]

    executor = ExecutionPlanner()

    tasks = executor.create_tasks(
        plan
    )

    assert len(tasks) > 0

    assert tasks[0].action in [
        "modify_component",
        "update_route",
        "run_tests",
    ]
