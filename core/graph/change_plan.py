from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from core.graph.change import ChangeRequest
from core.graph.signals import EngineeringSignal


class PlanStatus(str, Enum):
    CREATED = "created"
    READY = "ready"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class ChangePlan:

    change: ChangeRequest

    affected_nodes: list[str] = field(
        default_factory=list
    )

    signals: list[EngineeringSignal] = field(
        default_factory=list
    )

    execution_order: list[str] = field(
        default_factory=list
    )

    validation_steps: list[str] = field(
        default_factory=list
    )

    status: PlanStatus = PlanStatus.CREATED


    def add_signal(
        self,
        signal: EngineeringSignal,
    ) -> None:
        self.signals.append(signal)


    def add_affected_node(
        self,
        node_id: str,
    ) -> None:
        if node_id not in self.affected_nodes:
            self.affected_nodes.append(node_id)


    def add_validation(
        self,
        step: str,
    ) -> None:
        self.validation_steps.append(step)


    @property
    def signal_count(self) -> int:
        return len(self.signals)


    @property
    def affected_count(self) -> int:
        return len(self.affected_nodes)
