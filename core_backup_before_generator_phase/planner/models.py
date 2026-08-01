from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from core.planner.technology_plan import TechnologyPlan


# ============================================================
# Parsed Prompt
# ============================================================

@dataclass
class ParsedPrompt:
    """
    Raw information extracted from the user's prompt.
    """

    original: str

    project_name: str = ""

    description: str = ""

    keywords: List[str] = field(default_factory=list)

    project_type: str = ""

    style: str = ""

    domain: str = ""


# ============================================================
# Intent
# ============================================================

@dataclass
class Intent:
    """
    High-level intent inferred from the prompt.
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
# Planning Result
# ============================================================

@dataclass
class PlanningResult:
    """
    Final planning output before ProjectSpec creation.
    """

    parsed: ParsedPrompt

    intent: Intent

    architecture: str

    framework: str

    features: List[str] = field(
        default_factory=list
    )

    technologies: TechnologyPlan = field(
        default_factory=TechnologyPlan
    )

    confidence: float = 1.0

    notes: List[str] = field(
        default_factory=list
    )