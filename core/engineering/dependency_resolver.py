from __future__ import annotations

from dataclasses import dataclass, field

from core.engineering.requirements_analyzer import (
    ProjectRequirements,
)

from core.engineering.technology_selector import (
    TechnologyStack,
)


@dataclass(slots=True)
class DependencyManifest:
    """
    Complete dependency manifest for the project.
    """

    python: list[str] = field(default_factory=list)

    javascript: list[str] = field(default_factory=list)

    development: list[str] = field(default_factory=list)


class DependencyResolver:
    """
    Resolves project dependencies from the selected
    technology stack and project requirements.
    """

    def resolve(
        self,
        requirements: ProjectRequirements,
        stack: TechnologyStack,
    ) -> DependencyManifest:

        manifest = DependencyManifest()

        #
        # ----------------------------
        # Backend
        # ----------------------------
        #

        if stack.backend == "FastAPI":

            manifest.python.extend(
                [
                    "fastapi",
                    "uvicorn",
                    "pydantic",
                ]
            )

        #
        # ----------------------------
        # Database
        # ----------------------------
        #

        if stack.database == "PostgreSQL":

            manifest.python.extend(
                [
                    "sqlalchemy",
                    "psycopg2-binary",
                ]
            )

        elif stack.database == "SQLite":

            manifest.python.append(
                "sqlalchemy"
            )

        #
        # ----------------------------
        # Authentication
        # ----------------------------
        #

        if stack.authentication == "JWT":

            manifest.python.extend(
                [
                    "python-jose",
                    "passlib[bcrypt]",
                    "bcrypt",
                ]
            )

        #
        # ----------------------------
        # AI
        # ----------------------------
        #

        if requirements.ai:

            manifest.python.append(
                "openai"
            )

        #
        # ----------------------------
        # Frontend
        # ----------------------------
        #

        if stack.frontend == "React":

            manifest.javascript.extend(
                [
                    "react",
                    "react-dom",
                    "vite",
                ]
            )

        #
        # ----------------------------
        # Docker
        # ----------------------------
        #

        if stack.containerization:

            manifest.development.append(
                "docker"
            )

        #
        # ----------------------------
        # Testing
        # ----------------------------
        #

        manifest.development.extend(
            [
                "pytest",
                "pytest-cov",
            ]
        )

        #
        # Remove duplicates
        #

        manifest.python = sorted(
            set(manifest.python)
        )

        manifest.javascript = sorted(
            set(manifest.javascript)
        )

        manifest.development = sorted(
            set(manifest.development)
        )

        return manifest