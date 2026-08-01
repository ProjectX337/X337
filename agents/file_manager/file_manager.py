from __future__ import annotations

import os

from agents.base.base_agent import BaseAgent
from core.models.task_result import TaskResult
from core.projects.specification.project_spec import (
    ProjectSpec,
    GeneratedFile,
)


class FileManagerAgent(BaseAgent):

    AGENT_NAME = "FileManager"

    DESCRIPTION = (
        "Writes generated project files to disk."
    )

    CAPABILITIES = [
        "file_management"
    ]

    VERSION = "6.0.0"

    ENABLED = True

    def __init__(
        self,
        app=None,
    ):

        super().__init__(app=app)

        self.workspace = os.path.join(
            "workspace",
            "projects",
        )

    # =====================================================
    # Directories
    # =====================================================

    def create_project_directory(
        self,
        project_name: str,
    ) -> str:

        project_path = os.path.join(
            self.workspace,
            project_name,
        )

        os.makedirs(
            project_path,
            exist_ok=True,
        )

        return project_path

    # =====================================================
    # File Writing
    # =====================================================

    def write_generated_files(
        self,
        project_path: str,
        files: list[GeneratedFile],
    ) -> list[str]:

        written = []

        for file in files:

            full_path = os.path.join(
                project_path,
                file.path,
            )

            directory = os.path.dirname(
                full_path
            )

            if directory:

                os.makedirs(
                    directory,
                    exist_ok=True,
                )

            with open(
                full_path,
                "w",
                encoding="utf-8",
            ) as output:

                output.write(
                    file.content
                )

            if file.executable:

                os.chmod(
                    full_path,
                    0o755,
                )

            written.append(
                file.path
            )

        return written

    # =====================================================
    # Execute
    # =====================================================

    def execute(
        self,
        task,
    ):

        self.log(
            "Writing generated project..."
        )

        spec: ProjectSpec | None = self.recall(
            "project_spec"
        )

        if spec is None:

            return TaskResult(
                success=False,
                agent=self.name,
                task=task.title,
                result="ProjectSpec not found.",
            )

        project_path = self.create_project_directory(
            spec.name
        )

        created = self.write_generated_files(
            project_path,
            spec.files,
        )

        spec.path = project_path

        self.remember(
            "project_spec",
            spec,
        )

        task.history.append(
            "FileManager wrote generated files"
        )

        self.log(
            f"Wrote {len(created)} files."
        )

        return TaskResult(
            success=True,
            agent=self.name,
            task=task.title,
            result={
                "project": spec.name,
                "path": project_path,
                "files": created,
            },
        )
    