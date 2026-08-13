from __future__ import annotations

from core.graph.change import (
    ChangeRequest,
    ChangeType,
)

from core.graph.change_planner import ChangePlanner


class ChangeEngine:
    """
    Compatibility facade.

    Routes legacy change detection through
    the canonical graph evolution planner.
    """

    def __init__(
        self,
        planner: ChangePlanner | None = None,
    ):
        self.planner = planner


    def detect(
        self,
        graph,
        target_node: str,
    ):

        planner = (
            self.planner
            or ChangePlanner(graph)
        )

        request = ChangeRequest(
            target_node=target_node,
            change_type=ChangeType.MODIFY,
        )

        return planner.create_plan(
            request
        )