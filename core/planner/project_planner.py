from __future__ import annotations

from core.agent.capability_composer import CapabilityComposer
from core.agent.dependency_resolver import DependencyResolver


class ProjectPlanner:
    """
    Converts user intent into ordered capabilities.
    """

    def __init__(self):
        self.composer = CapabilityComposer()
        self.resolver = DependencyResolver()

    def plan(
        self,
        message: str,
    ) -> list[str]:

        capabilities = self.composer.compose(
            message
        )

        return self.resolver.resolve(
            capabilities
        )
