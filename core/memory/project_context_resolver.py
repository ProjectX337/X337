from __future__ import annotations

from core.memory.project_memory import ProjectMemory
from core.spec.project_spec import ProjectSpec
from core.spec.models.feature_spec import FeatureSpec
from core.planner.models import ParsedPrompt, Intent


class ProjectContextResolver:
    """
    Resolves the active project context for agent decisions.
    """

    def __init__(self):

        self.projects = ProjectMemory()


    def current(self):

        project = self.projects.current_project()

        if isinstance(project, dict):

            return self._restore_project(
                project
            )

        return project


    def enrich(
        self,
        message: str,
    ):

        return {
            "message": message,
            "project": self.current(),
        }


    def _restore_project(
        self,
        data,
    ):

        features = [
            FeatureSpec(
                name=f["name"],
                description=f.get(
                    "description",
                    "",
                ),
                routes=f.get(
                    "routes",
                    [],
                ),
                components=f.get(
                    "components",
                    [],
                ),
                state=f.get(
                    "state",
                    [],
                ),
                api_contracts=f.get(
                    "api_contracts",
                    [],
                ),
            )
            for f in data.get(
                "features",
                [],
            )
        ]


        parsed = ParsedPrompt(
            original=data.get(
                "description",
                "",
            ),
            project_name=data.get(
                "name",
                "x337-app",
            ),
            description=data.get(
                "description",
                "",
            ),
        )


        return ProjectSpec(
            prompt=data.get(
                "description",
                "",
            ),
            parsed=parsed,
            intent=Intent(),
            architecture=None,
            feature_models=features,
        )
