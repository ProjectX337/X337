from __future__ import annotations

from core.build.build_plan import BuildPlan
from core.spec.project_spec import ProjectSpec


class BuildPlanner:
    """
    Converts a ProjectSpec into an ordered BuildPlan.

    The architecture stack determines which generators are required.
    """

    def build(
        self,
        spec: ProjectSpec,
    ) -> BuildPlan:

        if spec.architecture is None:
            raise ValueError(
                "ProjectSpec is missing architecture. "
                "Run the planning pipeline before generation, "
                "or provide an ArchitectureStack explicitly."
            )

        architecture = spec.architecture

        plan = BuildPlan()

        if architecture.frontend:
            plan.add(
                name="Frontend",
                generator=architecture.frontend.lower(),
                description="Generate the frontend application",
                output_directory="frontend",
                priority=10,
            )

        if architecture.backend:
            plan.add(
                name="Backend",
                generator=architecture.backend.lower(),
                description="Generate the backend application",
                output_directory="backend",
                priority=20,
            )

        if architecture.ai:
            ai_dependencies: list[str] = []

            if architecture.backend:
                ai_dependencies.append("Backend")

            plan.add(
                name="AI",
                generator=architecture.ai.lower(),
                description="Generate AI components",
                output_directory="backend/ai",
                priority=30,
                depends_on=ai_dependencies,
            )

        if architecture.static_site:
            plan.add(
                name="Website",
                generator=architecture.static_site.lower(),
                description="Generate static website",
                output_directory="website",
                priority=40,
            )

        if architecture.scripting:
            plan.add(
                name="Utilities",
                generator=architecture.scripting.lower(),
                description="Generate utility scripts",
                output_directory="scripts",
                priority=50,
                optional=True,
            )

        return plan
