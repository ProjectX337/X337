from __future__ import annotations

from core.agent.change_plan import ChangePlan
from core.agent.feature_registry import FeatureRegistry


class ChangeEngine:
    """
    Converts user requests into project modifications.
    """

    def detect(
        self,
        message: str,
    ) -> dict:


        registry = FeatureRegistry()

        detected = registry.match(
            message
        )

        changes = detected


        plans = []


        for change in changes:

            capability = registry.get(
                change
            )


            if capability:

                plans.append(
                    ChangePlan(
                        feature=change,
                        routes=capability.get(
                            "routes",
                            []
                        ),
                        pages=capability.get(
                            "pages",
                            []
                        ),
                        components=capability.get(
                            "components",
                            []
                        ),
                        state=capability.get(
                            "state",
                            []
                        ),
                        api_contracts=capability.get(
                            "api_contracts",
                            []
                        ),
                    )
                )


            else:

                plans.append(
                    ChangePlan(
                        feature=change
                    )
                )


        return {
            "plans": plans
        }
