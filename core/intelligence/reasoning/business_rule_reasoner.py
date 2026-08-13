from __future__ import annotations

from core.intelligence.reasoning.business_rule_rules import (
    BUSINESS_RULES,
)


def infer_business_rules(
    domain: str,
) -> list[str]:

    return BUSINESS_RULES.get(
        domain,
        [],
    )
