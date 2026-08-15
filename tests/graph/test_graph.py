from core.graph.models import (
    ApplicationGraph,
    GraphNode,
    GraphEdge,
)


def test_graph():

    graph = ApplicationGraph()

    graph.add_node(
        GraphNode(
            id="intent",
            kind="intent",
            label="AI SaaS",
        )
    )

    graph.add_node(
        GraphNode(
            id="react",
            kind="technology",
            label="React",
        )
    )

    graph.add_edge(
        GraphEdge(
            source="intent",
            target="react",
            relation="requires",
        )
    )

    assert graph.get("intent").label == "AI SaaS"

    neighbors = graph.neighbors("intent")

    assert len(neighbors) == 1
    assert neighbors[0].id == "react"
    assert neighbors[0].label == "React"


if __name__ == "__main__":
    test_graph()
    print("✅ Graph passed")
