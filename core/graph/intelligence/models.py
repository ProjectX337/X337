from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class GraphInsight:
    """
    Reasoning output derived from ApplicationGraph.
    """

    capabilities: list[str] = field(
        default_factory=list
    )

    user_experiences: list[str] = field(
        default_factory=list
    )

    architecture_patterns: list[str] = field(
        default_factory=list
    )

    risks: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

    def as_dict(self) -> dict:
        return {
            "capabilities": self.capabilities,
            "user_experiences": self.user_experiences,
            "architecture_patterns": self.architecture_patterns,
            "risks": self.risks,
            "metadata": self.metadata,
        }
