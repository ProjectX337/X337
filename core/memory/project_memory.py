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
                    "name": f.name,
                    "description": f.description,
                    "routes": f.routes,
                    "components": f.components,
                    "state": f.state,
                    "api_contracts": f.api_contracts,
                }
                for f in spec.feature_models
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
