from core.decision.decision_graph import DecisionGraph
from core.decision.decision_node import DecisionNode
from core.decision.evidence_node import EvidenceNode


def test_decision_graph():

    graph = DecisionGraph()

    graph.add_decision(
        DecisionNode(
            id="tech",
            decision_type="technology",
            winner="React",
            confidence=0.96,
        )
    )

    graph.add_evidence(
        "tech",
        EvidenceNode(
            id="intent",
            source="Intent",
            message="Dashboard application",
            weight=5,
        ),
    )

    assert "tech" in graph.graph.nodes
    assert "intent" in graph.graph.nodes
    assert len(graph.graph.edges) == 1


if __name__ == "__main__":
    test_decision_graph()
    print("✅ DecisionGraph passed")
