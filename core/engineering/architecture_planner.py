from __future__ import annotations

from dataclasses import dataclass, field

from core.engineering.requirements_analyzer import (
    ProjectRequirements,
)

from core.engineering.technology_selector import (
    TechnologyStack,
)


@dataclass(slots=True)
class ArchitecturePlan:
    """
    Complete software architecture for a project.

    This is consumed by the ProjectGenerator and
    future engineering agents.
    """

    project_name: str = ""

    layers: list[str] = field(default_factory=list)

    folders: list[str] = field(default_factory=list)

    modules: list[str] = field(default_factory=list)

    services: list[str] = field(default_factory=list)

    configuration: list[str] = field(default_factory=list)

    testing: list[str] = field(default_factory=list)

    documentation: list[str] = field(default_factory=list)


class ArchitecturePlanner:
    """
    Builds the software architecture from the
    engineering requirements and technology stack.
    """

    def plan(
        self,
        requirements: ProjectRequirements,
        stack: TechnologyStack,
    ) -> ArchitecturePlan:

        plan = ArchitecturePlan()

        #
        # Root folders
        #

        plan.folders.extend(
            [
                "app",
                "config",
                "tests",
                "docs",
            ]
        )

        #
        # Backend
        #

        if stack.backend:

            plan.layers.extend(
                [
                    "API",
                    "Business",
                    "Persistence",
                ]
            )

            plan.folders.extend(
                [
                    "app/api",
                    "app/api/routes",
                    "app/models",
                    "app/schemas",
                    "app/services",
                    "app/repositories",
                    "app/core",
                ]
            )

            plan.modules.extend(
                [
                    "routes",
                    "schemas",
                    "database",
                    "settings",
                ]
            )

        #
        # Frontend
        #

        if stack.frontend:

            plan.folders.extend(
                [
                    "frontend",
                    "frontend/src",
                    "frontend/src/components",
                    "frontend/src/pages",
                    "frontend/public",
                ]
            )

            plan.modules.extend(
                [
                    "components",
                    "pages",
                ]
            )

        #
        # Database
        #

        if requirements.database:

            plan.services.append("Database")

        #
        # Authentication
        #

        if requirements.authentication:

            plan.services.append("Authentication")

        #
        # AI
        #

        if requirements.ai:

            plan.services.append("AI")

        #
        # Realtime
        #

        if requirements.realtime:

            plan.services.append("Realtime")

        #
        # Docker
        #

        if stack.containerization:

            plan.configuration.extend(
                [
                    "Dockerfile",
                    "docker-compose.yml",
                ]
            )

        #
        # Documentation
        #

        plan.documentation.extend(
            [
                "README.md",
                "API.md",
                "ARCHITECTURE.md",
            ]
        )

        #
        # Testing
        #

        plan.testing.extend(
            [
                "Unit Tests",
                "Integration Tests",
            ]
        )

        return plan