from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Capability:
    """
    Represents a reusable product capability.

    A capability is independent of any framework.
    Examples:
        - authentication
        - payments
        - realtime
        - notifications
        - search
        - ai_chat
    """

    name: str

    description: str = ""

    keywords: list[str] = field(default_factory=list)

    technologies: list[str] = field(default_factory=list)

    required_roles: list[str] = field(default_factory=list)

    priority: int = 100

    confidence: float = 1.0

    metadata: dict = field(default_factory=dict)
