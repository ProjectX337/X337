from __future__ import annotations

from core.graph.change_plan import ChangePlan
from core.execution.task import ExecutionTask


class ExecutionPlanner:
    """
    Converts ChangePlans into concrete
    execution tasks.

    Does not execute changes.
    """

    def create_tasks(
        self,
        plan: ChangePlan,
    ) -> list[ExecutionTask]:

        tasks = []

        for signal in plan.signals:

            tasks.append(
                ExecutionTask(
                    action=signal.signal_type.value,
                    target=signal.target_node,
                    metadata={
                        "change": (
                            plan.change.description
                        )
                    },
                )
            )

        return tasks
