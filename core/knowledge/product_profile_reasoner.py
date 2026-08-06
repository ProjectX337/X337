from __future__ import annotations

from core.knowledge.product_profile import ProductProfile
from core.knowledge.product_profiles import PRODUCT_PROFILES
from core.reasoning.base_reasoner import BaseReasoner
from core.reasoning.reasoning_kernel import ReasoningKernel


class ProductProfileReasoner(BaseReasoner):
    """
    Selects the best ProductProfile using the shared ReasoningKernel.
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

        # Fresh kernel for every inference
        self.kernel = ReasoningKernel()

        capability_names = {
            match.capability.name
            for match in capabilities
        }

        feature_names = {
            feature.slug
            for feature in features
        }

        for profile in PRODUCT_PROFILES.values():

            if intent:

                if getattr(intent, "ai", False) and profile.name == "AI SaaS":
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

        return next(
            profile
            for profile in PRODUCT_PROFILES.values()
            if profile.name == decision.winner
        )
