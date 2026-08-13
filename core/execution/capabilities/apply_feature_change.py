from __future__ import annotations

from core.execution.capability import (
    ExecutionCapability,
    ExecutionResult,
)

from core.spec.models.feature_spec import FeatureSpec


class ApplyFeatureChangeCapability(
    ExecutionCapability
):

    name = "apply_feature_change"


    def execute(
        self,
        task,
    ) -> ExecutionResult:

        project = task.metadata.get("project")
        plan = task.metadata.get("plan")

        if project is None or plan is None:
            return ExecutionResult(
                success=True,
                output={
                    "action": self.name,
                    "target": task.target,
                },
            )

        existing = None

        for feature in project.feature_models:

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

            project.feature_models.append(
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


        return ExecutionResult(
            success=True,
            output={
                "action": self.name,
                "feature": plan.feature,
            },
        )
