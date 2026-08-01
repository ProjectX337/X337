from __future__ import annotations

from core.capabilities.capability_registry import CapabilityRegistry
from core.planner.capability_match import CapabilityMatch
from core.planner.models import ParsedPrompt


class CapabilityPlanner:
    """
    Discovers and ranks capabilities for a prompt.

    The planner itself contains no hardcoded knowledge
    about authentication, payments, search, etc.

    All domain knowledge lives in capability JSON files.
    """

    def __init__(self):

        self.registry = CapabilityRegistry()

    # ---------------------------------------------------------

    def plan(
        self,
        parsed: ParsedPrompt,
    ) -> list[CapabilityMatch]:

        searchable = " ".join(
            [
                parsed.original,
                parsed.project_name,
                parsed.description,
                " ".join(parsed.keywords),
                parsed.project_type,
                parsed.style,
                parsed.domain,
            ]
        ).lower()

        scores: dict[str, tuple] = {}

        for word in searchable.split():

            for capability in self.registry.find_by_keyword(word):

                if capability.name not in scores:

                    scores[capability.name] = (
                        capability,
                        0,
                    )

                cap, score = scores[capability.name]

                scores[capability.name] = (
                    cap,
                    score + 1,
                )

        ranked = sorted(
            scores.values(),
            key=lambda item: (
                -item[1],
                -item[0].priority,
                item[0].name,
            ),
        )

        matches: list[CapabilityMatch] = []

        for capability, score in ranked:

            matches.append(

                CapabilityMatch(

                    capability=capability,

                    score=score,

                    confidence=min(
                        1.0,
                        score / 5,
                    ),

                )

            )

        return matches
