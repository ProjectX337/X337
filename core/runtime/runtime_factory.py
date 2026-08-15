from pathlib import Path

from core.runtime.project_runtime import ProjectRuntime


class RuntimeFactory:
    """
    Creates canonical ProjectRuntime objects.
    """

    def create(
        self,
        artifact,
        spec=None,
    ):

        if spec is None:
            spec = getattr(
                artifact,
                "spec",
                None
            )

        if spec is None:
            raise ValueError(
                "RuntimeFactory requires ProjectSpec"
            )

        runtime = ProjectRuntime(
            spec=spec,
            root_path=Path(
                artifact.path
            )
        )

        runtime.add_artifact(
            artifact.name,
            artifact
        )

        return runtime
