from __future__ import annotations

from collections import defaultdict

from core.knowledge.technology_registry import TECHNOLOGIES
from core.knowledge.technology_recommendation import TechnologyRecommendation


class TechnologyReasoner:

    def infer(

        self,

        *,

        intent,

        product_profile,

        architecture,

    ):

        scores = defaultdict(int)

        for tech in TECHNOLOGIES.values():

            if architecture:

                if architecture.name in tech.recommended_architectures:

                    scores[tech.name] += 5

            if product_profile:

                if product_profile.layout in tech.best_for:

                    scores[tech.name] += 3

            if intent:

                if getattr(intent, "ai", False):

                    if "ai" in tech.best_for:

                        scores[tech.name] += 6

                if getattr(intent, "website", False):

                    if "marketing" in tech.best_for:

                        scores[tech.name] += 4

        recommendations = []

        for tech in TECHNOLOGIES.values():

            score = scores[tech.name]

            recommendations.append(

                TechnologyRecommendation(

                    technology=tech,

                    score=score,

                    confidence=min(score / 10.0, 1.0),

                )

            )

        recommendations.sort(

            key=lambda r: r.score,

            reverse=True,

        )

        return recommendations
