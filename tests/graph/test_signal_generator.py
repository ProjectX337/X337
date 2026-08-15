from core.graph.signal_generator import SignalGenerator
from core.graph.models import (
    ApplicationGraph,
    GraphNode,
    NodeKind,
)
from core.graph.change import (
    ChangeRequest,
    ChangeType,
)
from core.graph.impact import ImpactReport
from core.graph.signals import SignalType


def test_signal_generation_from_change_impact():

    graph = ApplicationGraph()

    graph.add_node(
        GraphNode(
            id="page.login",
            kind=NodeKind.PAGE,
            name="Login",
        )
    )

    graph.add_node(
        GraphNode(
            id="component.form",
            kind=NodeKind.COMPONENT,
            name="Form",
        )
    )

    generator = SignalGenerator(graph)

    signals = generator.generate(
        ChangeRequest(
            target_node="feature.auth",
            change_type=ChangeType.MODIFY,
        ),
        ImpactReport(
            changed_node="feature.auth",
            affected_nodes=[
                "page.login",
                "component.form",
            ],
        ),
    )

    types = {
        signal.signal_type
        for signal in signals.signals
    }

    assert SignalType.MODIFY_COMPONENT in types
    assert SignalType.UPDATE_ROUTE in types
    assert SignalType.RUN_TESTS in types
