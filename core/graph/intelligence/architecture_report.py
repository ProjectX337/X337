from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ArchitectureReport:
    """
    Engineering analysis output
    derived from ApplicationGraph.
    """

    risks: list[str] = field(
        default_factory=list
    )

    warnings: list[str] = field(
        default_factory=list
    )

    recommendations: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

    def as_dict(self) -> dict:
        return {
            "risks": self.risks,
            "warnings": self.warnings,
            "recommendations": self.recommendations,
            "metadata": self.metadata,
        }
