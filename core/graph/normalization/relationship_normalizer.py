from __future__ import annotations

from core.graph.models import EdgeRelation


class RelationshipNormalizer:
    """
    Canonicalizes ApplicationGraph relationships.

    Responsibilities:
    - normalize relation enum values
    - remove duplicate edges
    - remove invalid edges
    """

    def normalize(
        self,
        graph,
    ):

        normalized = []

        seen = set()

        for edge in graph.edges:

            # -------------------------------
            # normalize relation
            # -------------------------------

            relation = edge.type

            if isinstance(
                relation,
                str,
            ):
                try:
                    relation = EdgeRelation(
                        relation
                    )
                except ValueError:
                    continue

                edge.type = relation


            # -------------------------------
            # remove invalid edges
            # -------------------------------

            if not edge.source:
                continue

            if not edge.target:
                continue

            if edge.source == edge.target:
                continue


            # -------------------------------
            # remove duplicates
            # -------------------------------

            identity = (
                edge.source,
                edge.target,
                edge.type,
            )

            if identity in seen:
                continue

            seen.add(identity)

            normalized.append(
                edge
            )


        graph.edges = normalized

        return graph
