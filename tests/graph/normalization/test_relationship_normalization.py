from core.graph.models import (
    GraphEdge,
    EdgeRelation,
)


from core.graph.normalization.relationship_normalizer import (
    RelationshipNormalizer,
)


class DummyGraph:

    def __init__(self):
        self.edges = []


def test_duplicate_relationships_are_removed():

    graph = DummyGraph()

    graph.edges = [
        GraphEdge(
            "feature.ai",
            "capability.ai",
            EdgeRelation.IMPLEMENTS,
        ),
        GraphEdge(
            "feature.ai",
            "capability.ai",
            EdgeRelation.IMPLEMENTS,
        ),
    ]


    RelationshipNormalizer().normalize(
        graph
    )


    assert len(graph.edges) == 1



def test_string_relations_are_normalized():

    graph = DummyGraph()

    graph.edges = [
        GraphEdge(
            "a",
            "b",
            "implements",
        )
    ]


    RelationshipNormalizer().normalize(
        graph
    )


    assert (
        graph.edges[0].relation
        == EdgeRelation.IMPLEMENTS
    )
