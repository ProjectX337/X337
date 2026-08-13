from __future__ import annotations

from core.planner.models import PlanningResult
from core.planner.project_planner import ProjectPlanner


class Planner:
    """
    Legacy compatibility adapter.

    The canonical planning engine is ProjectPlanner, which returns
    ProjectSpec. This class preserves the historical PlanningResult
    API without owning a second planning pipeline.
    """

    def __init__(self) -> None:
        self.project_planner = ProjectPlanner()

    def plan(self, prompt: str) -> PlanningResult:
        spec = self.project_planner.plan(prompt)

        return PlanningResult(
            parsed_prompt=spec.parsed,
            intent=spec.intent,
            technology_plan=spec.technologies,
            product_spec=getattr(
                spec,
                "product_spec",
                None,
            ),
            product_understanding=getattr(
                spec,
                "product_understanding",
                None,
            ),
            application_graph=getattr(
                spec,
                "application_graph",
                None,
            ),
            features=spec.feature_models,
        )
