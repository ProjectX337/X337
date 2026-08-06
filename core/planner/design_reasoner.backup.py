from __future__ import annotations

from core.planner.models import Intent
from core.planner.capability_match import CapabilityMatch
from core.spec.models.feature_spec import FeatureSpec
from core.spec.models.design_spec import DesignSpec


class DesignReasoner:
    """
    Infers a complete DesignSpec from planner outputs.

    This is the single source of design intelligence for X337.
    """

    def infer(
        self,
        *,
        intent: Intent | None,
        capabilities: list[CapabilityMatch],
        features: list[FeatureSpec],
        architecture=None,
        technologies=None,
    ) -> DesignSpec:

        design = DesignSpec()

        #
        # Layout
        #

        if intent:

            if getattr(intent, "dashboard", False):
                design.layout = "dashboard"

            elif getattr(intent, "website", False):
                design.layout = "marketing"

        #
        # Theme
        #

        if intent and getattr(intent, "ai", False):
            design.theme = "futuristic"
            design.typography = "technical"
            design.primary_color = "cyan"
            design.background = "dark"
            design.glassmorphism = True
            design.motion = "smooth"
            design.surface_style = "glass"

        #
        # Capability modifiers
        #

        capability_names = {
            c.capability.name
            for c in capabilities
        }

        if "authentication" in capability_names:
            design.radius = "medium"

        if "analytics" in capability_names:
            design.density = "compact"

        #
        # Feature modifiers
        #

        feature_names = {
            f.slug
            for f in features
        }

        if "chat" in feature_names:
            design.motion = "smooth"

        if "portfolio" in feature_names:
            design.spacing = "airy"

        return design
