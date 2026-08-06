from __future__ import annotations

from dataclasses import dataclass

from core.knowledge.technology_definition import TechnologyDefinition


@dataclass(slots=True)
class TechnologyRecommendation:

    technology: TechnologyDefinition

    score: int

    confidence: float
