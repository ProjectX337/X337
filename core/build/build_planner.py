from __future__ import annotations

from core.build.build_plan import BuildPlan
from core.spec.project_spec import ProjectSpec


class BuildPlanner:
    """
    Converts a ProjectSpec into an ordered BuildPlan.

    Dependencies are only created when the dependency
    actually exists in the generated build plan.
    """

    def build(
        self,
        spec: ProjectSpec,
    ) -> BuildPlan:

        plan = BuildPlan()

        if spec.architecture.frontend:
            plan.add(
                name="Frontend",
                generator=spec.architecture.frontend,
                description="Generate the frontend application",
                output_directory="frontend",
                priority=10,
            )

        if spec.architecture.backend:
            plan.add(
                name="Backend",
                generator=spec.architecture.backend,
                description="Generate the backend application",
                output_directory="backend",
                priority=20,
            )

        if spec.architecture.ai:
            ai_dependencies: list[str] = []

            if spec.architecture.backend:
                ai_dependencies.append("Backend")

            plan.add(
                name="AI",
                generator=spec.architecture.ai,
                description="Generate AI components",
                output_directory="backend/ai",
                priority=30,
                depends_on=ai_dependencies,
            )

        if spec.architecture.static_site:
            plan.add(
                name="Website",
                generator=spec.architecture.static_site,
                description="Generate static website",
                output_directory="website",
                priority=40,
            )

        if spec.architecture.scripting:
            plan.add(
                name="Utilities",
                generator=spec.architecture.scripting,
                description="Generate utility scripts",
                output_directory="scripts",
                priority=50,
                optional=True,
            )

        return plan
