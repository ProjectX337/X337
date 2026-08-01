from __future__ import annotations

from core.agent.feature_registry import FeatureRegistry


class FeatureGraph:
    """
    Resolves capability dependencies.
    """

    def __init__(self):
        self.registry = FeatureRegistry()


    def resolve(
        self,
        features: list[str],
    ) -> list[str]:

        resolved = []


        def visit(feature):

            if feature in resolved:
                return


            dependencies = self.registry.get(
                feature
            ).get(
                "dependencies",
                []
            )


            for dep in dependencies:
                visit(dep)


            resolved.append(feature)


        for feature in features:
            visit(feature)


        return resolved
