from __future__ import annotations

from dataclasses import dataclass

from core.spec.project_spec import ProjectSpec
from core.graph.change_plan import ChangePlan
from core.graph.models import ApplicationGraph
from core.execution.events.event_bus import ExecutionEventBus


@dataclass
class ExecutionContext:
    """
    Runtime context passed through execution.

    Contains the mutable application state
    required by execution capabilities.
    """

    project: ProjectSpec | None = None

    change_plan: ChangePlan | None = None

    application_graph: ApplicationGraph | None = None

    event_bus: ExecutionEventBus | None = None
