from dataclasses import dataclass

from .design_system import DesignSystem
from .layout_strategy import LayoutStrategy
from .component_strategy import ComponentStrategy


@dataclass
class DesignComposition:

    design_system: DesignSystem
    layout: LayoutStrategy
    components: ComponentStrategy


    def to_dict(self):

        return {
            "design_system": self.design_system.to_dict(),
            "layout": self.layout.to_dict(),
            "components": self.components.to_dict()
        }



class DesignComposer:


    def compose(self, product_type: str):

        design = DesignSystem(
            name="X337 Adaptive AI",
            visual_style="futuristic SaaS",
            theme="dark",
            product_type=product_type
        )


        layout = LayoutStrategy(
            page_type="adaptive_dashboard",
            structure=[
                "sidebar",
                "AI assistant",
                "progress tracking",
                "learning workspace",
                "analytics"
            ]
        )


        components = ComponentStrategy(
            component_type="AI learning interface",
            components=[
                "AITutorChat",
                "ProgressCard",
                "LearningModule",
                "AnalyticsPanel"
            ],
            interaction_level="high"
        )


        return DesignComposition(
            design_system=design,
            layout=layout,
            components=components
        )
