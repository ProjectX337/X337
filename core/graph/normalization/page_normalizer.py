from __future__ import annotations

from core.graph.models import NodeKind

from core.graph.normalization.page_identity import (
    normalize_page_slug,
)

from core.graph.normalization.identity_migration import (
    migrate_identity_keys,
)


class PageNormalizer:

    def normalize(
        self,
        graph,
    ):

        canonical = {}
        replacements = {}

        for node_id, node in list(
            graph.nodes.items()
        ):

            if node.type != NodeKind.PAGE:
                continue

            slug = normalize_page_slug(
                node_id.replace(
                    "page.",
                    "",
                )
            )

            canonical_id = (
                f"page.{slug}"
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
