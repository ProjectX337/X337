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

from core.intelligence.reasoning.quality_rules import (
    infer_quality_attributes,
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

        domain = infer_domain(text)

        return ProductIntent(
            domain=domain,

            goals=[
                parsed.description
            ]
            if parsed.description
            else [],

            workflows=infer_workflows(
                text
            ),

            capabilities=capabilities,

            quality_attributes=infer_quality_attributes(
                text,
                domain,
            ),

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
