from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class SignalType(str, Enum):
    MODIFY_COMPONENT = "modify_component"
    UPDATE_ROUTE = "update_route"
    UPDATE_API_CONTRACT = "update_api_contract"
    UPDATE_DATABASE = "update_database"
    RUN_TESTS = "run_tests"


@dataclass
class EngineeringSignal:
    """
    Represents engineering work inferred from
    ApplicationGraph changes.
    """

    signal_type: SignalType

    target_node: str

    metadata: dict = field(
        default_factory=dict
    )


@dataclass
class EngineeringSignalSet:

    signals: list[EngineeringSignal] = field(
        default_factory=list
    )

    def add(
        self,
        signal: EngineeringSignal,
    ) -> None:
        self.signals.append(signal)

    @property
    def count(self) -> int:
        return len(self.signals)
