from __future__ import annotations

from core.graph.change import (
    ChangeRequest,
    ChangeType,
)

from core.graph.change_planner import ChangePlanner


class ChangeEngine:
    """
    Compatibility facade.

    Historical agent API preserved while routing
    evolution planning through ApplicationGraph.
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
            or ChangePlanner()
        )

        request = ChangeRequest(
            target_node=target_node,
            change_type=ChangeType.MODIFY,
        )

        return planner.plan(
            graph,
            request,
        )
