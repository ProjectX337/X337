from __future__ import annotations

from core.projects.specification.project_spec import ProjectSpec
from core.registry.architecture_registry import ArchitectureRegistry


class DependencyResolver:
    """
    X337 Dependency Resolver

    Uses the ArchitectureRegistry as the source of truth
    for framework dependencies, then layers optional
    feature-specific dependencies on top.
    """

    def __init__(self):

        self.registry = ArchitectureRegistry()

    # ---------------------------------------------------------

    def resolve(
        self,
        spec: ProjectSpec,
    ) -> ProjectSpec:

        architecture = self.registry.get(spec.framework)

        #
        # Framework dependencies
        #

        for dependency in architecture.dependencies:
            spec.add_dependency(dependency)

        #
        # Optional features
        #

        features = spec.plan.get("features", [])

        if "authentication" in features:

            spec.add_dependency("python-jose")
            spec.add_dependency("passlib")
            spec.add_dependency("bcrypt")

        if "database" in features:

            spec.add_dependency("sqlalchemy")
            spec.add_dependency("alembic")

        if spec.plan.get("database") == "postgres":

            spec.add_dependency("psycopg2-binary")

        if "tests" in features:

            spec.add_dependency("pytest")

        if "docs" in features:

            spec.add_dependency("mkdocs")

        if "docker" in features:

            spec.add_dependency("gunicorn")

        spec.dependencies.sort()

        return spec