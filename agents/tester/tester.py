from __future__ import annotations

import os
import py_compile

from agents.base.base_agent import BaseAgent

from core.models.task_result import TaskResult

from core.events.event import Event
from core.events.event_types import EventTypes

from core.projects.specification.project_spec import ProjectSpec


class TesterAgent(BaseAgent):

    AGENT_NAME = "Tester"

    DESCRIPTION = (
        "Validates generated projects."
    )

    CAPABILITIES = [
        "testing"
    ]

    VERSION = "6.0.0"

    ENABLED = True

    def __init__(
        self,
        app=None,
    ):

        super().__init__(app=app)

    # =====================================================
    # Required Files
    # =====================================================

    REQUIRED = {
        "fastapi": [
            "app.py",
            "requirements.txt",
        ],
        "website": [
            "index.html",
            "style.css",
            "app.js",
        ],
        "frontend": [
            "index.html",
            "style.css",
            "app.js",
        ],
        "react": [
            "src/App.jsx",
        ],
    }

    def validate_files(
        self,
        spec: ProjectSpec,
    ) -> list[str]:

        required = self.REQUIRED.get(
            spec.framework.lower(),
            [],
        )

        missing = []

        for filename in required:

            path = os.path.join(
                spec.path,
                filename,
            )

            if not os.path.exists(path):

                missing.append(
                    filename
                )

        return missing

    # =====================================================
    # Python Syntax
    # =====================================================

    def validate_python(
        self,
        project_path: str,
    ) -> list[dict]:

        syntax_errors = []

        for root, _, files in os.walk(project_path):

            for file in files:

                if not file.endswith(".py"):
                    continue

                filepath = os.path.join(
                    root,
                    file,
                )

                try:

                    py_compile.compile(
                        filepath,
                        doraise=True,
                    )

                except Exception as exc:

                    syntax_errors.append(
                        {
                            "file": filepath,
                            "error": str(exc),
                        }
                    )

        return syntax_errors

    # =====================================================
    # Execute
    # =====================================================

    def execute(
        self,
        task,
    ):

        self.log(
            "Running project validation..."
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

        missing = self.validate_files(
            spec
        )

        syntax_errors = self.validate_python(
            spec.path
        )

        passed = (
            not missing
            and
            not syntax_errors
        )

        spec.tested = True

        self.remember(
            "project_spec",
            spec,
        )

        result = {

            "project": spec.name,

            "status":
                "passed"
                if passed
                else "failed",

            "missing_files": missing,

            "syntax_errors": syntax_errors,

            "files_tested": len(spec.files),

        }

        #
        # Save results for Reviewer
        #

        self.remember(
            "test_results",
            result,
        )

        task.history.append(
            "Tester validated generated project"
        )

        self.bus.publish(

            Event(

                EventTypes.TEST_COMPLETED,

                self.name,

                result,

            )

        )

        self.log(

            f"Validation {'passed' if passed else 'failed'}."

        )

        return TaskResult(

            success=passed,

            agent=self.name,

            task=task.title,

            result=result,

        )
