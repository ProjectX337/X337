from __future__ import annotations

from core.intelligence.models import ProductIntent
from core.planner.models import ParsedPrompt


class ProductIntentAnalyzer:
    """
    Converts parsed user input into canonical product intent.
    """

    def analyze(
        self,
        parsed: ParsedPrompt,
    ) -> ProductIntent:

        return ProductIntent(
            domain=self._infer_domain(parsed),
            goals=[
                parsed.description
            ]
            if parsed.description
            else [],
            capabilities=parsed.keywords,
            metadata={
                "source": "product_intent_analyzer",
                "project_name": parsed.project_name,
                "project_type": parsed.project_type,
                "style": parsed.style,
                "technologies": parsed.technologies,
            },
        )

    def _infer_domain(
        self,
        parsed: ParsedPrompt,
    ) -> str:

        text = parsed.original.lower()

        if any(
            word in text
            for word in [
                "student",
                "students",
                "learning",
                "education",
                "course",
                "teacher",
            ]
        ):
            return "education"

        return parsed.domain
