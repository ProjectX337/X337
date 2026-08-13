from __future__ import annotations


def migrate_identity_keys(
    graph,
    replacements: dict[str, str],
):
    """
    Migrates graph node dictionary keys after identity normalization.

    Handles:
    - node key replacement
    - duplicate canonical identities
    - preserving first canonical node
    """

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
