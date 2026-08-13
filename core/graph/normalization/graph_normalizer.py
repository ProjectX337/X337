from __future__ import annotations

from core.graph.normalization.feature_normalizer import (
    FeatureNormalizer,
)

from core.graph.normalization.relationship_normalizer import (
    RelationshipNormalizer,
)

from core.graph.normalization.page_normalizer import (
    PageNormalizer,
)


class GraphNormalizer:

    def normalize(
        self,
        graph,
    ):

        FeatureNormalizer().normalize(
            graph
        )

        PageNormalizer().normalize(
            graph
        )

        RelationshipNormalizer().normalize(
            graph
        )

        return graph



