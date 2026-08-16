from core.terminal.terminal_manager import TerminalManager
from core.runtime.process_manager import ProcessManager
from core.preview.runtime import PreviewRuntime
from core.runtime.runtime_factory import RuntimeFactory

import os
import time


class RuntimeManager:

    def __init__(
        self,
        registry=None,
        process_manager=None,
        preview_runtime=None,
    ):

        self.terminal = TerminalManager()

        if process_manager is None:
            raise ValueError(
                "RuntimeManager requires ProcessManager"
            )

        if preview_runtime is None:
            raise ValueError(
                "RuntimeManager requires PreviewRuntime"
            )

        self.process_manager = process_manager

        self.preview_runtime = preview_runtime

        self.runtime_factory = RuntimeFactory()

        if registry is None:
            raise ValueError(
                "RuntimeManager requires RuntimeRegistry"
            )

        self.runtime_registry = registry


    def launch(
        self,
        spec,
    ):

        if spec is None:
            raise ValueError(
                "RuntimeManager requires ProjectSpec"
            )

        root_path = spec.path

        if not root_path:
            root_path = os.path.join(
                "workspace",
                "generated",
                spec.slug,
            )

        if not os.path.isabs(root_path):
            root_path = os.path.abspath(
                root_path
            )

        os.makedirs(
            root_path,
            exist_ok=True
        )

        runtime = self.runtime_factory.create(
            spec=spec,
            root_path=root_path,
        )

        self.runtime_registry.register(
            runtime
        )

        stored_runtime = (
            self.runtime_registry.update_status(
                spec.project_name,
                "running",
            )
        )

        return {
            "runtime": stored_runtime,
            "processes": list(
                self.process_manager.list_runtime_processes().keys()
            ),
            "preview": runtime.preview,
        }


    def start_preview(
        self,
        project_slug
    ):

        preview = self.preview_runtime.start(
            project_slug
        )

        runtime = self.runtime_registry.update_preview(
            project_slug,
            preview,
        )

        self.runtime_registry.update_processes(
            project_slug,
            self.process_manager.list_runtime_processes(),
        )

        if runtime is None:
            raise ValueError(
                f"Runtime not found: {project_slug}"
            )

        return preview



    def stop(
        self,
        artifact_name
    ):

        stopped = self.process_manager.stop(
            artifact_name
        )


        return stopped



    def status(
        self,
        artifact_name
    ):

        return self.runtime_registry.get(
            artifact_name
        )


    def health(
        self,
        artifact_name
    ):

        runtime = self.runtime_registry.get(
            artifact_name
        )

        if runtime is None:
            return {
                "name": artifact_name,
                "healthy": False,
                "runtime": None,
            }

        health = runtime.get(
            "health",
            {}
        )

        return {
            "name": artifact_name,
            "healthy": (
                health.get(
                    "status"
                ) == "healthy"
            ),
            "runtime": runtime,
        }


    def update_status(
        self,
        artifact_name,
        status,
    ):

        return self.runtime_registry.update_status(
            artifact_name,
            status,
        )


    def previews(
        self
    ):

        return [
            runtime
            for runtime in self.runtime_registry.list()
            if runtime.get("preview")
        ]


    def list_running(
        self
    ):

        return self.runtime_registry.list()

