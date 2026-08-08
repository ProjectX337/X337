from core.features.feature_engine import (
    FeatureEngine
)

from core.planner.models import (
    ParsedPrompt
)

from core.templates.template_composer import (
    ApplicationBlueprint,
    PageBlueprint
)



class FeaturePlanner:
    """
    Converts discovered features
    into application blueprints.
    """


    def __init__(self):

        self.engine = FeatureEngine()



    def plan(
        self,
        prompt: ParsedPrompt
    ):


        features = (
            self.engine.analyze(
                prompt.original
            )
        )


        pages = []

        components = []

        services = []



        for feature in features:


            for page in feature.pages:

                pages.append(

                    PageBlueprint(

                        name=page,

                        route=
                        "/" +
                        page.lower(),

                        components=[]
                    )

                )



            components.extend(
                feature.components
            )


            services.extend(
                feature.services
            )



        for page in pages:

            page.components = (
                components
            )



        return {

            "features":
                features,

            "pages":
                pages,

            "components":
                list(
                    set(components)
                ),

            "services":
                list(
                    set(services)
                )

        }
