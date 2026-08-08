from core.templates.template_composer import (
    ApplicationBlueprint,
    PageBlueprint
)



class ApplicationAdapter:
    """
    Converts ApplicationPlan
    into ReactGenerator compatible
    ApplicationBlueprint.
    """



    def convert(
        self,
        application
    ):


        pages = []



        for page in application.pages:


            pages.append(

                PageBlueprint(

                    name=page.name,

                    route=page.route,

                    components=
                    application.components

                )

            )



        blueprint = ApplicationBlueprint(

            name=application.name,

            pages=pages,

            features=application.features

        )


        return blueprint