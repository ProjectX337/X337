from __future__ import annotations

from core.graph.models import NodeKind

from core.graph.normalization.feature_identity import (
    normalize_feature_slug,
)

from core.graph.normalization.identity_migration import (
    migrate_identity_keys,
)


class FeatureNormalizer:

    """
    Normalizes duplicate feature identities
    inside ApplicationGraph.
    """

    def normalize(
        self,
        graph,
    ):

        canonical = {}
        replacements = {}

        for node_id, node in list(
            graph.nodes.items()
        ):

            if node.kind != NodeKind.FEATURE:
                continue

            slug = normalize_feature_slug(
                node_id.replace(
                    "feature.",
                    "",
                )
            )

            canonical_id = (
                f"feature.{slug}"
            )

            if canonical_id not in canonical:

                canonical[
                    canonical_id
                ] = node

                replacements[
                    node_id
                ] = canonical_id

                node.id = canonical_id

                node.metadata.setdefault(
                    "aliases",
                    [],
                )

            else:

                existing = canonical[
                    canonical_id
                ]

                existing.metadata.setdefault(
                    "aliases",
                    [],
                )

                if node_id not in existing.metadata["aliases"]:
                    existing.metadata["aliases"].append(
                        node_id
                    )

                replacements[
                    node_id
                ] = canonical_id


        migrate_identity_keys(
            graph,
            replacements,
        )

        return graph
