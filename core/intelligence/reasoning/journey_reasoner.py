from __future__ import annotations

from core.intelligence.reasoning.journey_rules import (
    JOURNEY_RULES,
)


def infer_journeys(
    domain: str,
) -> list[dict]:

    return JOURNEY_RULES.get(
        domain,
        [],
    )
