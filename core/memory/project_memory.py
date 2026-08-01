from __future__ import annotations

from core.memory.memory_manager import MemoryManager


class ProjectMemory:
    """
    Stores and retrieves active X337 projects.
    """

    def __init__(self):

        self.memory = MemoryManager()



    def save_project(
        self,
        spec,
        build_result=None,
    ):

        data = {
            "name": spec.project_name,
            "description": spec.description,
            "features": [
                {
                    "name": feature.name,
                    "slug": feature.slug,
                    "description": feature.description,
                    "routes": feature.routes,
                      "pages": feature.pages,
                    "components": feature.components,
                    "state": feature.state,
                    "api_contracts": feature.api_contracts,
                }
                for feature in spec.feature_models
            ],
            "slug": spec.slug,
            "build": build_result,
        }

        self.memory.remember(
            "active_project",
            data,
        )

        return data


    def current_project(
        self,
    ):

        return self.memory.recall(
            "active_project"
        )
