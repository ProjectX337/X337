from __future__ import annotations

from core.agent.change_plan import ChangePlan
from core.agent.feature_registry import FeatureRegistry


class ChangeEngine:
    """
    Converts ordered capabilities into ChangePlans.
    """

    def __init__(self):
        self.registry = FeatureRegistry()


    def detect(
        self,
        features: list[str],
    ) -> dict:

        plans = []


        for feature in features:

            capability = self.registry.get(
                feature
            )


            if capability:

                plans.append(
                    ChangePlan(
                        feature=feature,
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


        return {
            "plans": plans
        }
