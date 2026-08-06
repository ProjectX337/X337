from __future__ import annotations

from core.agent.change_plan import ChangePlan
from core.spec.models.feature_spec import FeatureSpec


class ChangeEngine:
    """
    Converts FeatureSpec objects into ChangePlans.
    """

    def __init__(self):
        pass


    def detect(
        self,
        features: list[FeatureSpec],
    ) -> dict:

        plans = []

        for feature in features:

            plans.append(
                ChangePlan(
                    feature=feature.name,
                    routes=feature.routes,
                    pages=feature.pages,
                    components=feature.components,
                    state=feature.state,
                    api_contracts=feature.api_contracts,
                )
            )


        return {
            "plans": plans
        }
