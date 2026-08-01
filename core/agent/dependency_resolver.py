from __future__ import annotations


class DependencyResolver:
    """
    Expands features based on required dependencies.
    """


    DEPENDENCIES = {

        "dashboard": [
            "authentication",
        ],

        "analytics": [
            "dashboard",
        ],

        "billing": [
            "authentication",
        ],

    }


    def resolve(
        self,
        features: list[str],
    ) -> list[str]:

        resolved = []


        def add(feature):

            if feature in resolved:
                return


            for dependency in self.DEPENDENCIES.get(
                feature,
                []
            ):
                add(dependency)


            resolved.append(feature)


        for feature in features:
            add(feature)


        return resolved
