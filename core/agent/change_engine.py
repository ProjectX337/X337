from __future__ import annotations

from core.agent.change_plan import ChangePlan
from core.agent.feature_registry import FeatureRegistry
from core.agent.capability_composer import CapabilityComposer
from core.agent.feature_graph import FeatureGraph
from core.agent.feature_graph import FeatureGraph


class ChangeEngine:
    """
    Converts user requests into project modifications.
    """

    def detect(
        self,
        message: str,
    ) -> dict:


        registry = FeatureRegistry()

        composer = CapabilityComposer()

        graph = FeatureGraph()
        graph = FeatureGraph()

        detected = registry.match(
            message
        )

        composed = composer.compose(
            message
        )

        changes = list(
            dict.fromkeys(
                detected + composed
            )
        )

        changes = graph.resolve(
            changes
        )

        changes = graph.resolve(
            changes
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
