from core.intelligence.intelligence_runtime import (
    GraphIntelligenceRuntime,
)


class DummyGraph:
    def __init__(self):
        self.nodes = {
            "a": object(),
            "b": object(),
        }
        self.edges = [
            ("a", "b")
        ]


def test_graph_intelligence_runtime_contract():

    result = GraphIntelligenceRuntime(
        DummyGraph()
    ).analyze()

    assert result["node_count"] == 2
    assert result["edge_count"] == 1

    assert result["reasoning"] is not None
    assert result["architecture"] is not None
