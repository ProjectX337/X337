from __future__ import annotations

from core.intelligence.models import ProductUnderstanding


class CapabilityReasoner:
    """
    Infers product capabilities from product understanding.

    Converts:
        product goals + domain + entities + rules

    into:
        capability hypotheses
    """

    def reason(
        self,
        understanding: ProductUnderstanding,
    ) -> list[str]:

        capabilities = []

        domain = (
            understanding.domain.lower()
            if understanding.domain
            else ""
        )

        goals = " ".join(
            understanding.goals
        ).lower()

        if (
            "education" in domain
            or "tutor" in goals
            or "learning" in goals
        ):
            capabilities.extend(
                [
                    "adaptive tutoring",
                    "lesson generation",
                    "knowledge assessment",
                    "progress tracking",
                    "personalized recommendations",
                ]
            )

        if not capabilities:
            capabilities.append(
                "core product workflow"
            )

        return capabilities
