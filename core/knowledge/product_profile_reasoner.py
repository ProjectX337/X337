from __future__ import annotations

from core.knowledge.product_profile import ProductProfile
from core.knowledge.product_profiles import PRODUCT_PROFILES
from core.reasoning.base_reasoner import BaseReasoner
from core.reasoning.reasoning_kernel import ReasoningKernel


class ProductProfileReasoner(BaseReasoner):
    """
    Selects the best ProductProfile using the shared ReasoningKernel.

    Resolution is registry-based and defensive:
    the reasoning kernel may return an arbitrary decision label, while
    ProductProfile names are controlled by PRODUCT_PROFILES.
    """

    def __init__(self):
        self.kernel = ReasoningKernel()

    def infer(
        self,
        *,
        intent,
        capabilities,
        features,
    ) -> ProductProfile:

        # Fresh kernel for every inference.
        self.kernel = ReasoningKernel()

        capability_names = {
            match.capability.name
            for match in capabilities
            if getattr(match, "capability", None) is not None
        }

        feature_names = {
            feature.slug
            for feature in features
            if getattr(feature, "slug", None)
        }

        for profile in PRODUCT_PROFILES.values():

            if intent:

                if (
                    getattr(intent, "ai", False)
                    and profile.name == "AI SaaS"
                ):
                    self.kernel.vote(
                        profile.name,
                        weight=10,
                        source="Intent",
                        message="AI application",
                    )

                if (
                    getattr(intent, "dashboard", False)
                    and profile.layout == "dashboard"
                ):
                    self.kernel.vote(
                        profile.name,
                        weight=6,
                        source="Intent",
                        message="Dashboard project",
                    )

                if (
                    getattr(intent, "website", False)
                    and profile.layout == "marketing"
                ):
                    self.kernel.vote(
                        profile.name,
                        weight=6,
                        source="Intent",
                        message="Marketing website",
                    )

            capability_matches = len(
                capability_names.intersection(
                    profile.recommended_capabilities
                )
            )

            if capability_matches:
                self.kernel.vote(
                    profile.name,
                    weight=capability_matches * 3,
                    source="Capabilities",
                    message=f"{capability_matches} capability matches",
                )

            feature_matches = len(
                feature_names.intersection(
                    profile.required_features
                )
            )

            if feature_matches:
                self.kernel.vote(
                    profile.name,
                    weight=feature_matches * 2,
                    source="Features",
                    message=f"{feature_matches} feature matches",
                )

        decision = self.kernel.resolve()

        # ---------------------------------------------------------
        # Canonical registry resolution
        # ---------------------------------------------------------
        #
        # ReasoningKernel returns a decision label. ProductProfile
        # registry keys are the canonical lookup mechanism.
        #
        # Support both:
        #   "AI SaaS"  -> profile.name
        #   "ai_saas"  -> registry key
        #
        winner = decision.winner

        for profile in PRODUCT_PROFILES.values():
            if profile.name == winner:
                return profile

        normalized_winner = (
            str(winner)
            .strip()
            .lower()
            .replace("-", "_")
            .replace(" ", "_")
        )

        profile = PRODUCT_PROFILES.get(normalized_winner)

        if profile is not None:
            return profile

        # ---------------------------------------------------------
        # Defensive fallback
        # ---------------------------------------------------------
        #
        # A generic project may produce no votes. In that case the
        # reasoning kernel can return a label that is not a product
        # profile. Never allow that to crash planning.
        #
        fallback = PRODUCT_PROFILES.get("generic_application")

        if fallback is None:
            raise RuntimeError(
                "ProductProfile registry is missing "
                "'generic_application'; "
                f"winner={winner!r}"
            )

        return fallback
