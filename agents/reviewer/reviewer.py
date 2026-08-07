from __future__ import annotations

from agents.base.base_agent import BaseAgent

from core.models.task_result import TaskResult

from core.events.event import Event
from core.events.event_types import EventTypes

from core.spec.project_spec import ProjectSpec


class ReviewerAgent(BaseAgent):

    AGENT_NAME = "Reviewer"

    DESCRIPTION = (
        "Performs quality assurance on generated projects."
    )

    CAPABILITIES = [
        "review"
    ]

    VERSION = "6.0.0"

    ENABLED = True

    def __init__(
        self,
        app=None,
    ):
        super().__init__(
            app
        )

    # =====================================================
    # Score Calculation
    # =====================================================

    def calculate_score(
        self,
        spec: ProjectSpec,
        tests: dict,
    ) -> int:

        score = 100

        score -= len(
            tests.get(
                "missing_files",
                [],
            )
        ) * 20

        score -= len(
            tests.get(
                "syntax_errors",
                [],
            )
        ) * 25

        score -= len(
            getattr(
                spec,
                "warnings",
                [],
            )
        ) * 5

        score -= len(
            getattr(
                spec,
                "errors",
                [],
            )
        ) * 10

        score = max(
            score,
            0,
        )

        score = min(
            score,
            100,
        )

        return score

    # =====================================================
    # Review
    # =====================================================

    def execute(
        self,
        task,
    ):

        self.log(
            "Reviewing generated project..."
        )

        spec = self.recall(
            "project_spec"
        )

        if spec is None:

            return TaskResult(
                success=False,
                agent=self.name,
                task=task.title,
                result="ProjectSpec not found.",
            )

        tests = self.recall(
            "test_results"
        )

        if tests is None:

            return TaskResult(
                success=False,
                agent=self.name,
                task=task.title,
                result="No test results found.",
            )

        score = self.calculate_score(
            spec,
            tests,
        )

        spec.score = score

        spec.reviewed = True

        approved = (
            score >= 90
            and
            tests.get(
                "status"
            ) == "passed"
        )

        self.remember(
            "project_spec",
            spec,
        )

        result = {

            "project": spec.name,

            "approved": approved,

            "score": score,

            "warnings": getattr(
                spec,
                "warnings",
                [],
            ),

            "errors": getattr(
                spec,
                "errors",
                [],
            ),

            "generated_files": len(
                getattr(
                    spec,
                    "files",
                    [],
                )
            ),

            "framework": getattr(
                spec,
                "framework",
                None,
            ),

        }

        if approved:

            self.bus.publish(
                Event(
                    EventTypes.REVIEW_APPROVED,
                    self.name,
                    result,
                )
            )

        else:

            self.bus.publish(
                Event(
                    EventTypes.TASK_FAILED,
                    self.name,
                    result,
                )
            )

        self.bus.publish(
            Event(
                EventTypes.TASK_COMPLETED,
                self.name,
                result,
            )
        )

        task.history.append(
            "Reviewer completed project review"
        )

        self.log(
            f"Quality Score: {score}"
        )

        return TaskResult(
            success=approved,
            agent=self.name,
            task=task.title,
            result=result,
        )