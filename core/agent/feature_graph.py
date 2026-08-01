from __future__ import annotations


class FeatureGraph:
    """
    Represents relationships between project capabilities.
    """

    DEPENDENCIES = {
        "analytics": [
            "authentication",
            "dashboard",
        ],
        "dashboard": [
            "authentication",
        ],
        "billing": [
            "authentication",
        ],
        "authentication": [],
    }

    def resolve(
        self,
        features: list[str],
    ) -> list[str]:

        resolved = []

        def visit(feature):

            if feature in resolved:
                return

            for dep in self.DEPENDENCIES.get(
                feature,
                []
            ):
                visit(dep)

            resolved.append(feature)

        for feature in features:
            visit(feature)

        return resolved
