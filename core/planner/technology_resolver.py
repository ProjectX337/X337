from __future__ import annotations

from core.planner.stack_builder import ArchitectureStack
from core.planner.technology_plan import TechnologyPlan
from core.registry.architecture_registry import ArchitectureRegistry


class TechnologyResolver:
    """
    Builds a TechnologyPlan by merging the preferred
    technologies from each selected architecture.
    """

    def __init__(self):

        self.registry = ArchitectureRegistry()

    # ---------------------------------------------------------

    def resolve(
        self,
        stack: ArchitectureStack,
    ) -> TechnologyPlan:

        plan = TechnologyPlan()

        architecture_names = [
            stack.frontend,
            stack.backend,
            stack.ai,
            stack.static_site,
            stack.scripting,
            stack.mobile,
            stack.desktop,
            stack.testing,
        ]

        for name in architecture_names:

            if name is None:
                continue

            architecture = self.registry.get(name)

            if architecture is None:
                continue

            for key, value in architecture.technology_defaults.items():

                # Preserve the first selected technology.
                if getattr(plan, key, None) is None:

                    setattr(
                        plan,
                        key,
                        value,
                    )

        return plan