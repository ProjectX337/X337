from __future__ import annotations

from core.planner.models import Intent
from core.planner.capability_match import CapabilityMatch
from core.spec.ui_spec import UISpec


class UIPlanner:
    """
    Converts project intent into a UI blueprint.
    """

    def plan(
        self,
        *,
        intent: Intent,
        capabilities: list[CapabilityMatch],
    ) -> UISpec:

        pages = [
            "Landing",
        ]

        components = [
            "Navbar",
            "Button",
            "Card",
        ]

        layout = "default"


        capability_names = [
            capability.name
            for capability in capabilities
        ]


        if (
            "authentication"
            in capability_names
        ):

            pages.append(
                "Login"
            )


        if (
            intent
            and getattr(
                intent,
                "category",
                None,
            ) == "saas"
        ):

            pages.append(
                "Dashboard"
            )

            components.extend(
                [
                    "Sidebar",
                    "DataCard",
                ]
            )

            layout = "dashboard"


        return UISpec(
            pages=pages,
            components=components,
            layout=layout,
            theme="modern",
        )
