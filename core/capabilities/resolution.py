from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ResolvedCapability:
    name: str

    explicit: bool = False
    required: bool = False
    optional: bool = False

    confidence: float = 0.0

    evidence: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    implications: list[str] = field(default_factory=list)

    rationale: str = ""

    @property
    def committed(self) -> bool:
        return self.explicit or self.required