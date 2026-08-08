from core.planner.ui_blueprint import (
    UIBlueprint,
    UIPage
)


class UIPlannerBridge:


    def build_from_features(
        self,
        feature_spec,
        design_composition,
        application_name
    ):


        pages = []


        for page_name in feature_spec.pages:

            pages.append(
                UIPage(
                    name=page_name,
                    layout=design_composition.layout.page_type,
                    components=design_composition.components.components
                )
            )


        return UIBlueprint(

            application=application_name,

            pages=pages,

            theme={
                "mode": design_composition.design_system.theme,
                "style": design_composition.design_system.visual_style
            }
        )
