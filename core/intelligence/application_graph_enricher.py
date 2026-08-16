from __future__ import annotations

from pathlib import Path

from core.graph.models import (
    ApplicationGraph,
    GraphNode,
    GraphEdge,
    NodeKind,
    EdgeRelation,
)


class ApplicationGraphEnricher:
    """
    Enriches an ApplicationGraph with
    semantic application architecture.

    Source:
        discovered application structure

    Output:
        Feature/Page/Component relationships
    """

    def enrich(
        self,
        graph: ApplicationGraph,
        understanding: dict,
    ) -> ApplicationGraph:

        react = understanding.get(
            "react",
            {},
        )

        features = react.get(
            "features",
            [],
        )

        pages = react.get(
            "pages",
            [],
        )

        components = react.get(
            "components",
            [],
        )


        project_id = self._project_id(
            understanding
        )


        for feature in features:

            feature_id = (
                f"feature:{feature}"
            )

            graph.add_node(
                GraphNode(
                    id=feature_id,
                    kind=NodeKind.FEATURE,
                    name=feature,
                    metadata={
                        "source": "react_analyzer",
                    },
                )
            )

            graph.add_edge(
                GraphEdge(
                    source=project_id,
                    target=feature_id,
                    relation=EdgeRelation.CONTAINS,
                )
            )


        for page in pages:

            page_id = (
                f"page:{page}"
            )

            graph.add_node(
                GraphNode(
                    id=page_id,
                    kind=NodeKind.PAGE,
                    name=page,
                    metadata={
                        "source": "react_analyzer",
                    },
                )
            )

            graph.add_edge(
                GraphEdge(
                    source=project_id,
                    target=page_id,
                    relation=EdgeRelation.CONTAINS,
                )
            )


        for component in components:

            component_id = (
                f"component:{component}"
            )

            graph.add_node(
                GraphNode(
                    id=component_id,
                    kind=NodeKind.COMPONENT,
                    name=component,
                    metadata={
                        "source": "react_analyzer",
                    },
                )
            )

            graph.add_edge(
                GraphEdge(
                    source=project_id,
                    target=component_id,
                    relation=EdgeRelation.CONTAINS,
                )
            )


        self._connect_feature_files(
            graph,
            understanding,
        )


        return graph


    def _project_id(
        self,
        understanding,
    ) -> str:

        return (
            f"project:"
            f"{understanding['project']}"
        )


    def _connect_feature_files(
        self,
        graph,
        understanding,
    ):

        """
        Creates feature ownership edges
        from discovered paths.
        """

        files = understanding.get(
            "files",
            [],
        )

        for file in files:

            path = Path(file)

            if "features" not in path.parts:
                continue

            index = path.parts.index(
                "features"
            )

            if len(path.parts) <= index + 1:
                continue

            feature = path.parts[
                index + 1
            ]

            feature_id = (
                f"feature:{feature}"
            )

            file_id = (
                f"file:{file}"
            )

            if graph.has_node(
                feature_id
            ) and graph.has_node(
                file_id
            ):

                graph.add_edge(
                    GraphEdge(
                        source=feature_id,
                        target=file_id,
                        relation=EdgeRelation.IMPLEMENTS,
                    )
                )
