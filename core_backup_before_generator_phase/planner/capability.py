from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Capability:
    """
    Represents a product capability inferred from a prompt.

    Examples
    --------
    Authentication
    Payments
    Realtime
    AI Chat
    Notifications
    """

    name: str

    priority: int = 100

    confidence: float = 1.0

    technologies: list[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)
