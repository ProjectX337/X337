from __future__ import annotations

import re
import traceback

from agents.base.base_agent import BaseAgent

from core.models.task_result import TaskResult
from core.spec.project_spec import ProjectSpec

from core.events.event import Event
from core.events.event_types import EventTypes

from core.projects.project_generator import ProjectGenerator
from core.projects.dependency_resolver import DependencyResolver

from core.coding.code_planner import CodePlanner
from core.coding.software_architect import SoftwareArchitect


class CoderAgent(BaseAgent):

    AGENT_NAME = "Coder"

    DESCRIPTION = (
        "Plans, architects, and generates complete software projects."
    )

    CAPABILITIES = [
        "coding"
    ]

    VERSION = "6.0.0"

    ENABLED = True

    def __init__(
        self,
        app=None,
    ):

        super().__init__(app=app)

        self.code_planner = CodePlanner()
        self.architect = SoftwareArchitect()
        self.dependencies = DependencyResolver()
        self.generator = ProjectGenerator()

    # =====================================================
    # Execute
    # =====================================================

    def execute(
        self,
        task,
    ):

        try:

            self.log("Starting engineering pipeline...")

            # ------------------------------------------
            # Planning
            # ------------------------------------------

            plan = self.code_planner.analyze(task)

            self.log("Planning complete.")

            # ------------------------------------------
            # Project Specification
            # ------------------------------------------

            spec = task.project_spec

            if spec is None:

                return TaskResult(
                    success=False,
                    agent=self.name,
                    task=task.title,
                    result="Planner did not provide ProjectSpec.",
                )

            # ------------------------------------------
            # Architecture
            # ------------------------------------------

            self.log("Designing architecture...")

            spec = self.architect.design(spec)

            # ------------------------------------------
            # Dependencies
            # ------------------------------------------

            self.log("Resolving dependencies...")

            spec = self.dependencies.resolve(spec)

            # ------------------------------------------
            # Generation
            # ------------------------------------------

            self.log("Generating project...")

            spec = self.generator.generate(spec)

            # ------------------------------------------
            # Save memory
            # ------------------------------------------

            self.remember(
                "project_spec",
                spec,
            )

            self.remember(
                "code_plan",
                plan,
            )

            # ------------------------------------------
            # History
            # ------------------------------------------

            task.history.append(
                f"Generated project '{spec.name}'"
            )

            # ------------------------------------------
            # Event
            # ------------------------------------------

            self.bus.publish(
                Event(
                    EventTypes.CODE_GENERATED,
                    self.name,
                    spec.as_dict(),
                )
            )

            self.log(
                f"Generated {len(spec.files)} files."
            )

            return TaskResult(
                success=True,
                agent=self.name,
                task=task.title,
                result=spec.as_dict(),
            )

        except Exception as error:

            print("\n" + "=" * 80)
            print("CODER AGENT EXCEPTION")
            traceback.print_exc()
            print("=" * 80 + "\n")

            return TaskResult(
                success=False,
                agent=self.name,
                task=task.title,
                result=f"{type(error).__name__}: {error}",
            )

    # =====================================================
    # Utilities
    # =====================================================

    def create_project_name(
        self,
        title: str,
    ) -> str:

        title = re.sub(
            r"[^a-zA-Z0-9 ]",
            "",
            title,
        )

        return "_".join(
            title.lower().split()
        )
