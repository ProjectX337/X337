from __future__ import annotations

from core.graph.models import (
    NodeKind,
)

from core.graph.normalization.feature_identity import (
    normalize_feature_slug,
)


class GraphNormalizer:

    def normalize(self, graph):
        self._normalize_features(graph)
        return graph

    def _normalize_features(self, graph):

        canonical = {}

        replacements = {}

        for node_id, node in list(graph.nodes.items()):

            if node.kind != NodeKind.FEATURE:
                continue

            slug = normalize_feature_slug(
                node_id.replace("feature.", "")
            )

            canonical_id = f"feature.{slug}"

            if canonical_id not in canonical:
                canonical[canonical_id] = node
                replacements[node_id] = canonical_id
                node.id = canonical_id

                node.metadata.setdefault(
                    "aliases",
                    [],
                )

            else:
                existing = canonical[canonical_id]

                existing.metadata.setdefault(
                    "aliases",
                    [],
                )

                if node_id not in existing.metadata["aliases"]:
                    existing.metadata["aliases"].append(
                        node_id
                    )

                replacements[node_id] = canonical_id


        for old_id, new_id in replacements.items():

            if old_id != new_id:
                del graph.nodes[old_id]


        for edge in graph.edges:

            if edge.source in replacements:
                edge.source = replacements[edge.source]

            if edge.target in replacements:
                edge.target = replacements[edge.target]


        return graph
