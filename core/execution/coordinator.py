from __future__ import annotations

from dataclasses import dataclass, field

from core.graph.change_plan import ChangePlan
from core.execution.execution_planner import ExecutionPlanner
from core.execution.action_router import ActionRouter
from core.execution.capability import ExecutionResult
from core.execution.context.execution_context import ExecutionContext


@dataclass
class ExecutionReport:
    """
    Result of executing an evolution plan.
    """

    results: list[ExecutionResult] = field(
        default_factory=list
    )

    @property
    def success(self) -> bool:
        return all(
            result.success
            for result in self.results
        )


class ExecutionCoordinator:
    """
    Coordinates execution of ChangePlans.

    This is the runtime boundary between:
        planning
            |
            v
        execution
    """

    def __init__(
        self,
        router: ActionRouter,
        planner: ExecutionPlanner | None = None,
    ):

        self.router = router

        self.planner = (
            planner
            or ExecutionPlanner()
        )


    def execute(
        self,
        plan: ChangePlan,
        context: ExecutionContext | None = None,
    ) -> ExecutionReport:

        tasks = self.planner.create_tasks(
            plan,
            context=context,
        )

        results = []

        for task in tasks:

            result = self.router.execute(
                task
            )

            results.append(
                result
            )

        return ExecutionReport(
            results=results
        )
