from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class GraphChangeSet:
    added_nodes: list[str] = field(
        default_factory=list
    )

    removed_nodes: list[str] = field(
        default_factory=list
    )

    modified_nodes: list[str] = field(
        default_factory=list
    )

    added_edges: list[str] = field(
        default_factory=list
    )

    removed_edges: list[str] = field(
        default_factory=list
    )


@dataclass
class ImpactReport:
    affected_nodes: list[str] = field(
        default_factory=list
    )

    severity: str = "low"

    metadata: dict = field(
        default_factory=dict
    )


@dataclass
class EvolutionPlan:
    actions: list[str] = field(
        default_factory=list
    )

    priority: str = "normal"

    metadata: dict = field(
        default_factory=dict
    )
