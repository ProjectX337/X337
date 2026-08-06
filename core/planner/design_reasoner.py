from __future__ import annotations

from core.planner.models import Intent
from core.planner.capability_match import CapabilityMatch
from core.spec.models.feature_spec import FeatureSpec
from core.spec.models.design_spec import DesignSpec
from core.knowledge.product_profile import ProductProfile

from core.reasoning.base_reasoner import BaseReasoner
from core.reasoning.reasoning_kernel import ReasoningKernel


class DesignReasoner(BaseReasoner):
    """
    Infers a DesignSpec using the shared ReasoningKernel.

    The kernel aggregates evidence while this class translates the
    winning decisions into a concrete DesignSpec.
    """

    def infer(
        self,
        *,
        intent: Intent | None,
        capabilities: list[CapabilityMatch],
        features: list[FeatureSpec],
        product_profile: ProductProfile | None = None,
        architecture=None,
        technologies=None,
    ) -> DesignSpec:

        layout_kernel = ReasoningKernel()
        theme_kernel = ReasoningKernel()
        spacing_kernel = ReasoningKernel()
        motion_kernel = ReasoningKernel()

        #
        # Product Profile
        #

        if product_profile:

            layout_kernel.vote(
                product_profile.layout,
                weight=100,
                source="ProductProfile",
                message="Canonical layout",
            )

            theme_kernel.vote(
                product_profile.theme,
                weight=100,
                source="ProductProfile",
                message="Canonical theme",
            )

            spacing_kernel.vote(
                product_profile.density,
                weight=100,
                source="ProductProfile",
                message="Canonical spacing",
            )

            motion_kernel.vote(
                product_profile.motion,
                weight=100,
                source="ProductProfile",
                message="Canonical motion",
            )

        #
        # Intent
        #

        if intent:

            if getattr(intent, "dashboard", False):

                layout_kernel.vote(
                "dashboard",
                weight=5,
                source="Intent",
                message="Dashboard project",
            )

                spacing_kernel.vote(
                "compact",
                weight=2,
                source="Intent",
                message="Dashboard density",
            )

            if getattr(intent, "website", False):

                layout_kernel.vote(
                "marketing",
                weight=5,
                source="Intent",
                message="Website",
            )

                spacing_kernel.vote(
                "comfortable",
                weight=2,
                source="Intent",
                message="Website spacing",
            )

            if getattr(intent, "ai", False):

                theme_kernel.vote(
                "futuristic",
                weight=6,
                source="Intent",
                message="AI product",
            )

                motion_kernel.vote(
                "smooth",
                weight=3,
                source="Intent",
                message="AI interactions",
            )

        #
        # Capabilities
        #

        for match in capabilities:

            name = match.capability.name

            if name == "authentication":

                spacing_kernel.vote(
                "comfortable",
                weight=1,
                source="Capability",
                message="Authentication",
            )

            elif name == "analytics":

                layout_kernel.vote(
                "dashboard",
                weight=3,
                source="Capability",
                message="Analytics",
            )

            elif name == "chat":

                motion_kernel.vote(
                "smooth",
                weight=2,
                source="Capability",
                message="Chat",
            )

        #
        # Features
        #

        for feature in features:

            if feature.slug == "portfolio":

                layout_kernel.vote(
                "marketing",
                weight=2,
                source="Feature",
                message="Portfolio",
            )

                spacing_kernel.vote(
                "airy",
                weight=4,
                source="Feature",
                message="Portfolio",
            )

            elif feature.slug == "dashboard":

                layout_kernel.vote(
                "dashboard",
                weight=4,
                source="Feature",
                message="Dashboard",
            )

        #
        # Resolve
        #

        layout = layout_kernel.resolve().winner
        theme = theme_kernel.resolve().winner
        spacing = spacing_kernel.resolve().winner
        motion = motion_kernel.resolve().winner

        design = DesignSpec()

        design.layout = layout
        design.theme = theme
        design.spacing = spacing
        design.density = spacing
        design.motion = motion

        #
        # Theme presets
        #

        if theme == "futuristic":

            design.primary_color = "cyan"
            design.background = "dark"
            design.typography = "technical"
            design.glassmorphism = True
            design.surface_style = "glass"

        elif theme == "modern":

            design.primary_color = "blue"

        return design
