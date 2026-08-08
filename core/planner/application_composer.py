from dataclasses import dataclass, field

from core.planner.feature_planner import (
    FeaturePlanner
)

from core.templates.template_composer import (
    ApplicationBlueprint,
    PageBlueprint
)



@dataclass
class ApplicationPlan:

    name: str

    pages: list = field(
        default_factory=list
    )

    components: list[str] = field(
        default_factory=list
    )

    services: list[str] = field(
        default_factory=list
    )

    features: list[str] = field(
        default_factory=list
    )



class ApplicationComposer:
    """
    Combines features into a complete
    application architecture.
    """


    def __init__(self):

        self.feature_planner = (
            FeaturePlanner()
        )



    def compose(
        self,
        prompt
    ):


        result = (
            self.feature_planner.plan(
                prompt
            )
        )



        feature_names = []


        for feature in result["features"]:

            feature_names.append(
                feature.name
            )



        blueprint = ApplicationPlan(

            name="generated_app",

            pages=result["pages"],

            components=result["components"],

            services=result["services"],

            features=feature_names

        )


        return blueprint