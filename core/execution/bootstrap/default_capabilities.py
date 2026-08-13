from __future__ import annotations

from core.execution.action_router import ActionRouter

from core.execution.capabilities.modify_component import (
    ModifyComponentCapability,
)

from core.execution.capabilities.update_route import (
    UpdateRouteCapability,
)

from core.execution.capabilities.run_tests import (
    RunTestsCapability,
)


def create_default_router() -> ActionRouter:

    router = ActionRouter()

    router.register(
        "modify_component",
        ModifyComponentCapability(),
    )

    router.register(
        "update_route",
        UpdateRouteCapability(),
    )

    router.register(
        "run_tests",
        RunTestsCapability(),
    )

    return router
