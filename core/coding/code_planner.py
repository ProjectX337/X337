from __future__ import annotations

from core.registry.architecture_registry import ArchitectureRegistry


class CodePlanner:
    """
    X337 Code Planner

    Determines the most appropriate architecture
    for a user's request using the ArchitectureRegistry.

    The planner is intentionally lightweight—it does not
    know about FastAPI, React, or any other framework.
    All framework knowledge comes from the registry.
    """

    def __init__(self):

        self.registry = ArchitectureRegistry()

    # ---------------------------------------------------------
    # Main Analysis
    # ---------------------------------------------------------

    def analyze(
        self,
        task,
    ) -> dict:

        title = task.title.lower()

        architecture = self._select_architecture(title)

        plan = {
            "framework": architecture.name,
            "language": architecture.language,
            "database": self._default_database(architecture.name),
            "features": architecture.default_features.copy(),
            "files": [],
        }

        return plan

    # ---------------------------------------------------------
    # Architecture Selection
    # ---------------------------------------------------------

    def _select_architecture(
        self,
        title: str,
    ):

        for architecture in self.registry.all():

            for keyword in architecture.keywords:

                if keyword.lower() in title:

                    return architecture

        #
        # Fallback
        #

        return self.registry.get("python")

    # ---------------------------------------------------------
    # Default Database
    # ---------------------------------------------------------

    def _default_database(
        self,
        framework: str,
    ):

        defaults = {

            "fastapi": "sqlite",

            "django": "sqlite",

            "flask": "sqlite",

            "ai_agent": None,

            "react": None,

            "website": None,

            "python": None,

        }

        return defaults.get(framework)

    # ---------------------------------------------------------
    # Explain Decision
    # ---------------------------------------------------------

    def explain(
        self,
        task,
    ) -> str:

        plan = self.analyze(task)

        return (
            f"Framework: {plan['framework']}\n"
            f"Language: {plan['language']}\n"
            f"Database: {plan['database']}\n"
            f"Features: {', '.join(plan['features']) or 'None'}"
        )

