from __future__ import annotations

from core.intelligence.models import ProductUnderstanding
from core.intelligence.artifacts.capability_hypothesis import (
    CapabilityHypothesis,
)


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
    ) -> list[CapabilityHypothesis]:

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
                    CapabilityHypothesis(
                        name="adaptive tutoring",
                        confidence=0.8,
                        source="capability_reasoner",
                    ),
                    CapabilityHypothesis(
                        name="lesson generation",
                        confidence=0.8,
                        source="capability_reasoner",
                    ),
                    CapabilityHypothesis(
                        name="knowledge assessment",
                        confidence=0.8,
                        source="capability_reasoner",
                    ),
                    CapabilityHypothesis(
                        name="progress tracking",
                        confidence=0.8,
                        source="capability_reasoner",
                    ),
                    CapabilityHypothesis(
                        name="personalized recommendations",
                        confidence=0.8,
                        source="capability_reasoner",
                    ),
                ]
            )

        if not capabilities:
            capabilities.append(
                CapabilityHypothesis(
                    name="core product workflow",
                    confidence=0.5,
                    source="capability_reasoner",
                )
            )

        return capabilities
