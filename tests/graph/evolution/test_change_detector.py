from core.graph.models import (
    ApplicationGraph,
    GraphNode,
    NodeKind,
)

from core.graph.evolution.change_detector import (
    ChangeDetector,
)


def test_detect_added_node():

    before = ApplicationGraph()

    after = ApplicationGraph()

    after.add_node(
        GraphNode(
            id="component.mfa",
            type=NodeKind.COMPONENT,
            name="MFA",
        )
    )

    result = ChangeDetector().detect(
        before,
        after,
    )

    assert (
        "component.mfa"
        in result.added_nodes
    )
