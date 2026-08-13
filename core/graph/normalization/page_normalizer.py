from __future__ import annotations

from core.graph.models import NodeKind

from core.graph.normalization.page_identity import (
    normalize_page_slug,
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

            if node.kind != NodeKind.PAGE:
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


        for old_id, new_id in replacements.items():

            if old_id == new_id:
                continue

            node = graph.nodes.pop(
                old_id
            )

            if new_id not in graph.nodes:
                graph.nodes[new_id] = node


        for edge in graph.edges:

            if edge.source in replacements:
                edge.source = replacements[
                    edge.source
                ]

            if edge.target in replacements:
                edge.target = replacements[
                    edge.target
                ]


        return graph
