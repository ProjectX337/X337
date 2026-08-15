from __future__ import annotations

from pathlib import Path

from core.runtime.project_runtime import ProjectRuntime
from core.spec.project_spec import ProjectSpec


class RuntimeFactory:
    """
    Creates canonical ProjectRuntime objects.

    ProjectSpec is the source of application identity.
    """

    def create(
        self,
        spec: ProjectSpec,
        root_path: str | Path,
    ) -> ProjectRuntime:

        if spec is None:
            raise ValueError(
                "RuntimeFactory requires ProjectSpec"
            )

        runtime = ProjectRuntime(
            spec=spec,
            root_path=Path(root_path),
        )

        return runtime
