from __future__ import annotations

from core.intelligence.models import ProductIntent
from core.planner.models import ParsedPrompt


class ProductIntentAnalyzer:
    """
    Converts parsed user input into canonical product intent.

    Initial implementation is deterministic.
    Future versions can incorporate LLM reasoning.
    """

    def analyze(
        self,
        parsed: ParsedPrompt,
    ) -> ProductIntent:

        return ProductIntent(
            domain=parsed.domain,

            goals=[
                parsed.description
            ]
            if parsed.description
            else [],

            capabilities=list(
                parsed.keywords
            ),

            metadata={
                "source": "product_intent_analyzer",
                "project_name": parsed.project_name,
                "project_type": parsed.project_type,
                "style": parsed.style,
            },
        )
