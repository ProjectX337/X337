from core.planner.ui_blueprint import (
    UIBlueprint,
    UIPage
)


class UIBlueprintBuilder:


    def build(self, composition, application_name):


        page = UIPage(

            name="Dashboard",

            layout=composition.layout.page_type,

            components=composition.components.components

        )


        return UIBlueprint(

            application=application_name,

            pages=[
                page
            ],

            theme={
                "mode": composition.design_system.theme,
                "style": composition.design_system.visual_style
            }

        )
