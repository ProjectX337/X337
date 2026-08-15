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

        capabilities: list[CapabilityHypothesis] = []

        domain = (
            understanding.domain.lower()
            if understanding.domain
            else ""
        )

        goals = " ".join(
            understanding.goals
        ).lower()

        # -----------------------------------------------------
        # Canonical capability vocabulary
        #
        # Product understanding may contain natural-language
        # capability terms such as "assistant". Normalize those
        # terms into canonical registry capability names.
        # -----------------------------------------------------

        vocabulary = {
            "assistant": "ai",
            "ai assistant": "ai",
            "llm": "ai",
            "copilot": "ai",
            "auth": "authentication",
            "login": "authentication",
            "signin": "authentication",
            "signup": "authentication",
            "analytics": "analytics",
            "dashboard": "dashboard",
            "users": "users",
            "user management": "users",
            "search": "search",
            "chat": "chat",
            "messaging": "chat",
            "billing": "billing",
            "payments": "payments",
            "payment": "payments",
            "settings": "settings",
            "calendar": "calendar",
            "tasks": "tasks",
            "notifications": "notifications",
            "reports": "reporting",
            "reporting": "reporting",
            "admin": "admin",
            "administration": "admin",
            "teams": "team_management",
            "team management": "team_management",
            "file upload": "file_upload",
            "upload": "file_upload",
            "crm": "crm",
        }

        # -----------------------------------------------------
        # Direct capabilities from canonical understanding.
        # -----------------------------------------------------

        for value in understanding.capabilities:
            normalized = value.strip().lower()

            canonical = vocabulary.get(
                normalized,
                normalized,
            )

            if canonical in {
                "and",
                "or",
                "the",
                "a",
                "an",
            }:
                continue

            capabilities.append(
                CapabilityHypothesis(
                    name=canonical,
                    confidence=0.9,
                    source="capability_reasoner",
                    evidence=[value],
                )
            )

        # -----------------------------------------------------
        # Goal/domain inference remains additional intelligence.
        # -----------------------------------------------------

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

        # -----------------------------------------------------
        # Stable fallback only when intelligence found nothing.
        # -----------------------------------------------------

        if not capabilities:
            capabilities.append(
                CapabilityHypothesis(
                    name="core product workflow",
                    confidence=0.5,
                    source="capability_reasoner",
                )
            )

        # -----------------------------------------------------
        # Deduplicate while preserving strongest evidence.
        # -----------------------------------------------------

        deduplicated: dict[str, CapabilityHypothesis] = {}

        for hypothesis in capabilities:
            existing = deduplicated.get(
                hypothesis.name
            )

            if existing is None:
                deduplicated[hypothesis.name] = hypothesis
                continue

            if hypothesis.confidence > existing.confidence:
                deduplicated[hypothesis.name] = hypothesis

            elif hypothesis.evidence:
                existing.evidence.extend(
                    evidence
                    for evidence in hypothesis.evidence
                    if evidence not in existing.evidence
                )

        return list(
            deduplicated.values()
        )
