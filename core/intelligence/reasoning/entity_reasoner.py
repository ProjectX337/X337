from __future__ import annotations

from core.intelligence.reasoning.entity_rules import ENTITY_RULES


def infer_entities(
    domain: str,
) -> list[str]:

    return ENTITY_RULES.get(
        domain,
        [],
    )
