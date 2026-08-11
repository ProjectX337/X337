from __future__ import annotations

from dataclasses import dataclass

from core.cognition.cognitive_state import CognitiveState


class PlanningPipelineError(RuntimeError):
    """Raised when the planning pipeline violates its contracts."""


@dataclass(frozen=True)
class StageExecution:
    name: str
    requires: frozenset[str]
    provides: frozenset[str]


class PlanningPipeline:

    def __init__(self, stages):
        self.stages = list(stages)
        self._validate_stage_graph()

    # ---------------------------------------------------------
    # Static validation
    # ---------------------------------------------------------

    def _validate_stage_graph(self) -> None:
        available: set[str] = set()

        for stage in self.stages:
            missing = stage.requires - available

            if missing:
                raise PlanningPipelineError(
                    f"Invalid planning pipeline.\n"
                    f"Stage: {stage.__class__.__name__}\n"
                    f"Missing inputs: {sorted(missing)}\n"
                    f"Available outputs: {sorted(available)}"
                )

            overlap = stage.provides & available

            if overlap:
                raise PlanningPipelineError(
                    f"Duplicate pipeline outputs.\n"
                    f"Stage: {stage.__class__.__name__}\n"
                    f"Already provided: {sorted(overlap)}"
                )

            available.update(stage.provides)

    # ---------------------------------------------------------
    # Runtime validation
    # ---------------------------------------------------------

    def _validate_requirements(
        self,
        stage,
        state: CognitiveState,
        completed: set[str],
    ) -> None:

        missing = stage.requires - completed

        if missing:
            raise PlanningPipelineError(
                f"Stage dependency failure.\n"
                f"Stage: {stage.__class__.__name__}\n"
                f"Missing: {sorted(missing)}\n"
                f"Completed: {sorted(completed)}"
            )

    # ---------------------------------------------------------
    # Execution
    # ---------------------------------------------------------

    def run(
        self,
        state: CognitiveState,
    ) -> CognitiveState:

        completed: set[str] = set()

        for stage in self.stages:

            self._validate_requirements(
                stage,
                state,
                completed,
            )

            stage.run(state)

            completed.update(stage.provides)

        return state
