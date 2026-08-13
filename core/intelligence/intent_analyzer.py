from __future__ import annotations

from core.intelligence.models import ProductIntent
from core.planner.models import ParsedPrompt

from core.intelligence.reasoning.domain_rules import (
    infer_domain,
)

from core.intelligence.reasoning.workflow_rules import (
    infer_workflows,
)

from core.intelligence.reasoning.capability_rules import (
    infer_capabilities,
)


class ProductIntentAnalyzer:
    """
    Converts parsed user input into canonical product intent.

    This class coordinates reasoning modules.
    It does not contain domain intelligence.
    """

    def analyze(
        self,
        parsed: ParsedPrompt,
    ) -> ProductIntent:

        text = parsed.original

        capabilities = list(
            dict.fromkeys(
                [
                    *parsed.keywords,
                    *infer_capabilities(text),
                ]
            )
        )

        return ProductIntent(
            domain=infer_domain(text),

            goals=[
                parsed.description
            ]
            if parsed.description
            else [],

            workflows=infer_workflows(
                text
            ),

            capabilities=capabilities,

            metadata={
                "source": (
                    "product_intent_analyzer"
                ),
                "project_name": (
                    parsed.project_name
                ),
                "project_type": (
                    parsed.project_type
                ),
                "style": (
                    parsed.style
                ),
                "technologies": (
                    parsed.technologies
                ),
            },
        )
