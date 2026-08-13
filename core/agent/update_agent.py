from __future__ import annotations

from core.agent.project_state import ProjectState
from core.agent.change_engine import ChangeEngine
from core.planner.project_planner import ProjectPlanner

from core.execution.coordinator import ExecutionCoordinator
from core.execution.bootstrap.default_capabilities import (
    create_default_router,
)
from core.execution.execution_state import ExecutionState
from core.execution.context.execution_context import ExecutionContext


class UpdateAgent:
    """
    Applies changes to an existing project.
    """

    def __init__(self):

        self.state = ProjectState()

        self.engine = ChangeEngine()

        self.planner = ProjectPlanner()

        self.executor = ExecutionCoordinator(
            router=create_default_router()
        )

        self.execution_state = ExecutionState()


    def apply(
        self,
        message: str,
        context=None,
    ):

        project = None

        if context:

            if isinstance(context, dict):

                project = context.get(
                    "project"
                )

            else:

                project = getattr(
                    context,
                    "spec",
                    None,
                )

        if project:

            self.state.update(
                project
            )

        spec = self.planner.plan(
            message
        )

        changes = self.engine.detect(
            spec.feature_models
        )

        for plan in changes["plans"]:

            self.state.record_change(
                plan
            )

            execution_context = ExecutionContext(
                project=self.state.project,
                change_plan=plan,
            )

            report = self.executor.execute(
                plan,
                context=execution_context,
            )

            for result in report.results:
                self.execution_state.record(
                    result
                )


        return self.state

