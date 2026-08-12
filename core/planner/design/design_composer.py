from __future__ import annotations

from dataclasses import dataclass

from core.knowledge.product_profile import ProductProfile

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
    Produces coherent design intelligence from a canonical
    ProductProfile.

    ProductProfile is authoritative for product-level design
    decisions. The composer translates that profile into the
    design models consumed by the UI planner and blueprint builder.
    """

    def compose(
        self,
        *,
        product_profile: ProductProfile,
    ) -> DesignComposition:

        profile = product_profile

        design = DesignSystem(
            name="X337 Adaptive AI",
            visual_style=(
                "futuristic SaaS"
                if profile.theme == "futuristic"
                else "modern"
            ),
            theme=profile.theme,
            product_type=profile.name,
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
            page_type=profile.layout,
            structure=(
            list(profile.layout_sections)
            if profile.layout_sections
            else (
                [
                    "Header",
                    "Sidebar",
                    "Content",
                    "Footer",
                ]
                if profile.layout == "dashboard"
                else (
                    [
                        "Navbar",
                        "Hero",
                        "Content",
                        "Footer",
                    ]
                    if profile.layout == "marketing"
                    else [
                        "Header",
                        "Content",
                        "Footer",
                    ]
                )
            )
        ),
            layout_pattern=profile.layout,
            navigation=profile.navigation,
            density=profile.density,
            responsive_behavior="adaptive",
            user_flow=list(profile.navigation_items),
        )

        components = ComponentStrategy(
            component_type=f"{profile.name} interface",
            components=list(profile.default_components),
            interaction_level=(
                "high"
                if profile.motion == "smooth"
                else "standard"
            ),
            animation_behavior=profile.motion,
            responsive_behavior="adaptive",
            state_management="local",
        )

        return DesignComposition(
            design_system=design,
            layout=layout,
            components=components,
        )
