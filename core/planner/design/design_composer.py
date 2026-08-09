from __future__ import annotations

from dataclasses import dataclass

from .design_system import DesignSystem
from .layout_strategy import LayoutStrategy
from .component_strategy import ComponentStrategy


@dataclass(slots=True)
class DesignComposition:
    design_system: DesignSystem
    layout: LayoutStrategy
    components: ComponentStrategy

    def to_dict(self):
        return {
            "design_system": self.design_system.to_dict(),
            "layout": self.layout.to_dict(),
            "components": self.components.to_dict(),
        }


class DesignComposer:
    """
    Produces coherent design intelligence for an application.
    """

    def compose(self, product_type: str) -> DesignComposition:

        design = DesignSystem(
            name="X337 Adaptive AI",
            visual_style="futuristic SaaS",
            theme="dark",
            product_type=product_type,
            colors={
                "background": "#0B1020",
                "surface": "#111827",
                "primary": "#7C3AED",
                "secondary": "#06B6D4",
                "accent": "#22D3EE",
                "text": "#F8FAFC",
                "muted": "#94A3B8",
            },
            typography={
                "heading": "Inter",
                "body": "Inter",
                "mono": "JetBrains Mono",
            },
            spacing={
                "unit": "4px",
                "section": "64px",
                "container": "1200px",
            },
            color_palette=[
                "#0B1020",
                "#111827",
                "#7C3AED",
                "#06B6D4",
                "#22D3EE",
            ],
        )

        layout = LayoutStrategy(
            page_type="adaptive_dashboard",
            structure=[
                "sidebar",
                "AI assistant",
                "progress tracking",
                "learning workspace",
                "analytics",
            ],
        )

        components = ComponentStrategy(
            component_type="AI learning interface",
            components=[
                "AITutorChat",
                "ProgressCard",
                "LearningModule",
                "AnalyticsPanel",
            ],
            interaction_level="high",
        )

        return DesignComposition(
            design_system=design,
            layout=layout,
            components=components,
        )
