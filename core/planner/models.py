from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from core.planner.technology_plan import TechnologyPlan
from core.spec.models.feature_spec import FeatureSpec
from core.spec.models.design_system import DesignSystem


# ============================================================
# Parsed User Prompt
# ============================================================

@dataclass
class ParsedPrompt:
    """
    Raw information extracted from the user's request.
    """

    original: str

    project_name: str = ""

    description: str = ""

    keywords: List[str] = field(
        default_factory=list
    )

    project_type: str = ""

    style: str = ""

    domain: str = ""

    technologies: list[str] = field(
        default_factory=list
    )


# ============================================================
# User Intent
# ============================================================

@dataclass
class Intent:
    """
    Determines what the project requires.
    """

    frontend: bool = False
    backend: bool = False
    database: bool = False
    authentication: bool = False
    deployment: bool = False
    testing: bool = False
    documentation: bool = False
    api: bool = False
    website: bool = False
    dashboard: bool = False
    ai: bool = False


# ============================================================
# Final Planning Result
# ============================================================

@dataclass
class PlanningResult:
    """
    Complete output from the legacy planner API.

    FeatureSpec is the canonical feature domain model.
    imported from their owning packages.
    """

    parsed_prompt: ParsedPrompt

    intent: Intent

    technology_plan: TechnologyPlan = field(
        default_factory=TechnologyPlan
    )


    features: List[FeatureSpec] = field(
        default_factory=list
    )
