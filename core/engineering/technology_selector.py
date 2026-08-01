from __future__ import annotations

from dataclasses import dataclass

from core.engineering.requirements_analyzer import (
    ProjectRequirements,
)


@dataclass(slots=True)
class TechnologyStack:
    """
    Selected technology stack for a project.
    """

    frontend: str = ""

    backend: str = ""

    database: str = ""

    orm: str = ""

    authentication: str = ""

    testing: str = ""

    deployment: str = ""

    containerization: str = ""

    documentation: str = ""

    realtime: str = ""

    ai: str = ""

    package_manager: str = ""


class TechnologySelector:
    """
    Chooses the best technology stack
    from structured project requirements.
    """

    def select(
        self,
        requirements: ProjectRequirements
    ) -> TechnologyStack:

        stack = TechnologyStack()

        #
        # ----------------------------
        # Frontend
        # ----------------------------
        #

        if requirements.website:

            stack.frontend = "React"

            stack.package_manager = "npm"

        #
        # ----------------------------
        # Backend
        # ----------------------------
        #

        if requirements.api:

            stack.backend = "FastAPI"

        #
        # ----------------------------
        # Database
        # ----------------------------
        #

        if requirements.database:

            stack.database = "PostgreSQL"

            stack.orm = "SQLAlchemy"

        else:

            stack.database = "SQLite"

            stack.orm = "SQLAlchemy"

        #
        # ----------------------------
        # Authentication
        # ----------------------------
        #

        if requirements.authentication:

            stack.authentication = "JWT"

        #
        # ----------------------------
        # Testing
        # ----------------------------
        #

        stack.testing = "Pytest"

        #
        # ----------------------------
        # Deployment
        # ----------------------------
        #

        if requirements.docker:

            stack.containerization = "Docker"

            stack.deployment = "Docker Compose"

        #
        # ----------------------------
        # Documentation
        # ----------------------------
        #

        stack.documentation = "OpenAPI"

        #
        # ----------------------------
        # AI
        # ----------------------------
        #

        if requirements.ai:

            stack.ai = "OpenAI"

        #
        # ----------------------------
        # Realtime
        # ----------------------------
        #

        if requirements.realtime:

            stack.realtime = "WebSockets"

        return stack