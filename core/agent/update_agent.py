from __future__ import annotations

from core.agent.project_state import ProjectState
from core.agent.change_engine import ChangeEngine
from core.spec.models.feature_spec import FeatureSpec
from core.planner.project_planner import ProjectPlanner

from core.execution.coordinator import ExecutionCoordinator
from core.execution.bootstrap.default_capabilities import (
    create_default_router,
)
from core.execution.execution_state import ExecutionState


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

            report = self.executor.execute(
                plan
            )

            for result in report.results:
                self.execution_state.record(
                    result
                )


            if not self.state.project:
                continue


            existing = None


            for feature in self.state.project.feature_models:

                if feature.name == plan.feature:
                    existing = feature
                    break


            if existing:

                existing.routes = plan.routes
                existing.pages = plan.pages
                existing.components = plan.components
                existing.state = plan.state
                existing.api_contracts = plan.api_contracts


            else:

                self.state.project.feature_models.append(
                    FeatureSpec(
                        name=plan.feature,
                        slug=plan.feature,
                        description=f"{plan.feature} feature",
                        routes=plan.routes,
                        pages=plan.pages,
                        components=plan.components,
                        state=plan.state,
                        api_contracts=plan.api_contracts,
                    )
                )


        return self.state

